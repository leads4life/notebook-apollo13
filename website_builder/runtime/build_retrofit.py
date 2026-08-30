#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup
import argparse, json, shutil, base64, mimetypes

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_BASE=ROOT/'reference/ATLANTIC-MERIDIAN-BASELINE.html'

def set_text(node, text):
    if node is not None: node.string=str(text)

def copy_img(src, out, name):
    p=Path(src).expanduser().resolve()
    if not p.exists(): raise SystemExit(f'Missing image: {p}')
    dest=out/'assets/images'/(name+p.suffix.lower())
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,dest)
    return str(dest.relative_to(out)).replace('\\','/')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('spec')
    ap.add_argument('--output', required=True)
    ap.add_argument('--self-contained', action='store_true')
    a=ap.parse_args()
    spec=json.loads(Path(a.spec).read_text())
    baseline = spec.get('retrofit_baseline') or spec.get('approved_reference')
    BASE = Path(baseline).expanduser().resolve() if baseline else DEFAULT_BASE
    if not BASE.exists():
        raise SystemExit('Retrofit mode requires an approved baseline. Set retrofit_baseline in the spec or add reference/ATLANTIC-MERIDIAN-BASELINE.html')
    if len(spec['subcategories'])!=6 or len(spec['proof'])!=3 or len(spec['faq'])!=4 or len(spec['decision']['checklist'])!=4:
        raise SystemExit('Spec violates baseline cardinality contract')
    out=Path(a.output).resolve(); out.mkdir(parents=True,exist_ok=True)
    soup=BeautifulSoup(BASE.read_text(errors='ignore'),'html.parser')
    cat=spec['category']; brand=spec['brand']; hero=spec['hero']
    if soup.title: soup.title.string=spec.get('title',f"{cat} Website Design Company")
    for m in soup.find_all('meta'):
        if m.get('name')=='description': m['content']=spec.get('meta_description',hero['body'])
    paths={}
    paths['hero']=copy_img(hero['image'],out,'hero')
    for i,x in enumerate(spec['subcategories'],1): paths[f'sub{i}']=copy_img(x['image'],out,f'sub-{i}')
    paths['decision']=copy_img(spec['decision']['image'],out,'decision')
    paths['showcase']=copy_img(spec['showcase']['image'],out,'showcase')
    if spec.get('avatar'): paths['avatar']=copy_img(spec['avatar'],out,'avatar')
    top=soup.select('.topline span'); set_text(top[0],brand['label']); set_text(top[1],brand['topline'])
    set_text(soup.select_one('.brand-mark'),brand.get('mark','WD')); set_text(soup.select_one('.brand b'),brand['label']); set_text(soup.select_one('.brand small'),brand['subtitle'])
    hs=soup.select_one('section.hero'); hs.select_one('img.hero-media')['src']=paths['hero']; hs.select_one('img.hero-media')['alt']=f'{cat} website design showcase'
    set_text(hs.select_one('.eyebrow'),hero['eyebrow']); h1=hs.select_one('h1'); h1.clear(); h1.append(hero['h1_prefix']+' '); em=soup.new_tag('em'); em.string=hero['h1_emphasis']; h1.append(em)
    set_text(hs.select_one('.hero-copy p'),hero['body'])
    for el,txt in zip(hs.select('.hero-facts span'),hero['facts']): set_text(el,txt)
    intro=soup.select_one('#marine-websites'); intro['id']='category-websites'; set_text(intro.select_one('.eyebrow'),spec['intro']['eyebrow']); set_text(intro.select_one('h2'),spec['intro']['h2'])
    for el,k in zip(intro.select('.prose p'),['p1','p2']): set_text(el,spec['intro'][k])
    band=soup.select_one('#yacht-dealers'); band['id']='category-types'
    for i,(art,x) in enumerate(zip(band.find_all('article',recursive=False),spec['subcategories']),1):
        art.select_one('img')['src']=paths[f'sub{i}']; art.select_one('img')['alt']=x['title']; set_text(art.select_one('span'),f'{i:02}'); set_text(art.select_one('h3'),x['title']); set_text(art.select_one('p'),x['description'])
    d=soup.select_one('#shipyards'); d['id']='category-conversion'; set_text(d.select_one('.eyebrow'),spec['decision']['eyebrow']); set_text(d.select_one('h2'),spec['decision']['h2']); set_text(d.select_one('p'),spec['decision']['body'])
    for el,txt in zip(d.select('.checklist li'),spec['decision']['checklist']): set_text(el,txt)
    d.select_one('img')['src']=paths['decision']; d.select_one('img')['alt']=spec['decision'].get('alt',spec['decision']['h2']); set_text(d.select_one('figcaption'),spec['decision']['figcaption'])
    sh=soup.select_one('#showcase'); sh.select_one('img')['src']=paths['showcase']; sh.select_one('img')['alt']=spec['showcase']['showcase_name']+' website showcase'; set_text(sh.select_one('.eyebrow'),spec['showcase']['eyebrow']); set_text(sh.select_one('h2'),spec['showcase']['h2'])
    for el,k in zip(sh.find_all('p'),['p1','p2']): set_text(el,spec['showcase'][k])
    seo=soup.select_one('#marine-seo'); seo['id']='category-seo'; set_text(seo.select_one('.eyebrow'),spec['seo']['eyebrow']); set_text(seo.select_one('h2'),spec['seo']['h2'])
    for el,k in zip(seo.select('.prose p'),['p1','p2']): set_text(el,spec['seo'][k])
    for art,x in zip(soup.select_one('.proof-grid').find_all('article',recursive=False),spec['proof']): set_text(art.select_one('span'),x['number']); set_text(art.select_one('h2'),x['h2']); set_text(art.select_one('p'),x['body'])
    r=soup.select_one('#redesign'); set_text(r.select_one('.eyebrow'),spec['redesign']['eyebrow']); set_text(r.select_one('h2'),spec['redesign']['h2'])
    for el,k in zip(r.select('.prose p'),['p1','p2']): set_text(el,spec['redesign'][k])
    f=soup.select_one('#faq'); set_text(f.select_one('.eyebrow'),spec.get('faq_eyebrow','BUYER QUESTIONS')); set_text(f.select_one('h2'),spec.get('faq_h2',f'Before you choose a {cat.lower()} website design company.'))
    for det,x in zip(f.select('.faq-grid details'),spec['faq']): set_text(det.select_one('summary'),x['question']); set_text(det.select_one('p'),x['answer'])
    p=spec['proposal']; cta=soup.select_one('#proposal'); set_text(cta.select_one('.eyebrow'),p['eyebrow']); set_text(cta.select_one('h2'),p['h2'])
    ps=soup.select_one('#proposal-form'); pc=ps.select_one('.proposal-copy'); set_text(pc.select_one('h2'),p['project_h2']); pars=pc.find_all('p',recursive=False); set_text(pars[0],p['project_p1']); set_text(pars[1],p['best_fit'])
    labels=ps.select('form label'); sel=labels[3].find('select'); labels[3].contents[0].replace_with(p['sector_label']); sel.clear()
    for v in p['sector_options']:
        o=soup.new_tag('option'); o.string=v; sel.append(o)
    ps.find('textarea')['placeholder']=p['textarea_placeholder']
    foot=soup.select_one('.site-footer'); set_text(foot.select_one('.footer-brand'),brand['label']); set_text(foot.find_all('p')[0],spec['footer']['description']); set_text(foot.select('.footer-bottom span')[0],spec['footer']['bottom_label']); set_text(foot.select('.footer-bottom span')[1],spec['footer']['bottom_categories'])
    av=paths.get('avatar',paths['decision'])
    for img in soup.select('.joy-launcher img, .joy-head img'): img['src']=av
    (out/'index.html').write_text(str(soup))
    (out/'CATEGORY-SPEC.json').write_text(json.dumps(spec,indent=2))
    if a.self_contained:
        pv=BeautifulSoup(str(soup),'html.parser')
        for img in pv.find_all('img'):
            src=img.get('src','')
            pth=out/src
            if src.startswith('assets/') and pth.exists():
                mime=mimetypes.guess_type(pth.name)[0] or 'application/octet-stream'; img['src']='data:'+mime+';base64,'+base64.b64encode(pth.read_bytes()).decode()
        (out/'preview.html').write_text(str(pv))
    print(out)
if __name__=='__main__': main()
