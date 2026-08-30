#!/usr/bin/env python3
from pathlib import Path
import argparse, base64, html, json, mimetypes, shutil

CSS = r'''
:root{--ink:#1f211d;--paper:#f6f0e4;--accent:#9e4a2f;--deep:#20352d;--gold:#c69a56;--line:rgba(31,33,29,.18);--max:1180px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.6}a{color:inherit}.wrap{width:min(calc(100% - 40px),var(--max));margin:auto}.site-header{position:absolute;z-index:20;inset:0 0 auto;color:white;border-bottom:1px solid rgba(255,255,255,.25)}.nav{min-height:84px;display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{text-decoration:none;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.navlinks{display:flex;gap:22px;flex-wrap:wrap}.navlinks a{text-decoration:none;font:600 13px/1.2 Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase}.hero{min-height:88vh;display:grid;align-items:end;position:relative;color:white;background:#111;overflow:hidden}.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.68}.hero:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.18),rgba(0,0,0,.72))}.hero-copy{position:relative;z-index:2;padding:160px 0 80px;max-width:800px}.eyebrow{font:700 12px/1.2 Arial,sans-serif;letter-spacing:.18em;text-transform:uppercase}.hero h1,.page-hero h1{font-size:clamp(46px,8vw,94px);line-height:.92;margin:.15em 0 .25em;letter-spacing:-.045em}.hero p{font-size:clamp(18px,2.2vw,25px);max-width:690px}.cta{display:inline-block;margin-top:18px;padding:14px 20px;border:1px solid currentColor;text-decoration:none;font:700 13px/1 Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase}.page-hero{padding:150px 0 70px;background:var(--deep);color:white}.page-hero h1{font-size:clamp(42px,7vw,78px)}main section{padding:74px 0}.intro{font-size:clamp(23px,3vw,36px);line-height:1.25;max-width:900px}.split{display:grid;grid-template-columns:1.05fr .95fr;gap:54px;align-items:center}.split img{width:100%;height:460px;object-fit:cover}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.card{border-top:1px solid var(--line);padding:24px 0}.card h3{font-size:24px;margin:.2em 0}.section-title{font-size:clamp(34px,5vw,58px);line-height:1;margin:.15em 0 .6em}.footer{background:#171915;color:#eee;padding:54px 0}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:30px}.muted{opacity:.75}.gallery{display:grid;grid-template-columns:repeat(12,1fr);gap:12px}.gallery img{width:100%;height:320px;object-fit:cover;grid-column:span 4}.gallery img:nth-child(4n+1){grid-column:span 7}.gallery img:nth-child(4n+2){grid-column:span 5}.contact{display:grid;grid-template-columns:1fr 1fr;gap:30px}.contact-box{border:1px solid var(--line);padding:28px}button.menu{display:none;background:none;border:1px solid rgba(255,255,255,.5);color:white;padding:10px}
@media(max-width:800px){.wrap{width:min(calc(100% - 28px),var(--max))}.nav{min-height:70px}.navlinks{display:none;position:absolute;top:70px;left:14px;right:14px;background:#171915;padding:20px;flex-direction:column}.navlinks.open{display:flex}button.menu{display:block}.hero{min-height:78vh}.hero-copy{padding:130px 0 54px}.split,.contact,.footer-grid{grid-template-columns:1fr}.cards{grid-template-columns:1fr}.split img{height:340px}.gallery{grid-template-columns:1fr}.gallery img,.gallery img:nth-child(n){grid-column:auto;height:280px}}
'''

JS = "document.querySelector('.menu')?.addEventListener('click',()=>document.querySelector('.navlinks')?.classList.toggle('open'));"

def esc(x): return html.escape(str(x or ''))

def copy_img(src, out, stem):
    if not src: return ''
    p=Path(src).expanduser().resolve()
    if not p.exists(): raise SystemExit(f'Missing image: {p}')
    dest=out/'assets/images'/(stem+p.suffix.lower())
    dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dest)
    return str(dest.relative_to(out)).replace('\\','/')

def data_uri(p):
    mime=mimetypes.guess_type(p.name)[0] or 'application/octet-stream'
    return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()

def head(title, desc, css_path='assets/css/site.css'):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><link rel="stylesheet" href="{css_path}"></head><body>'''

def nav(spec):
    b=spec['business']; links=''.join(f'<a href="{esc(x["file"])}">{esc(x["label"])}</a>' for x in spec['navigation'])
    return f'''<header class="site-header"><div class="wrap nav"><a class="brand" href="index.html">{esc(b['name'])}</a><button class="menu" aria-label="Menu">Menu</button><nav class="navlinks">{links}</nav></div></header>'''

def footer(spec):
    b=spec['business']; contact=[]
    if b.get('phone'): contact.append(f'<div>{esc(b["phone"])}</div>')
    if b.get('email'): contact.append(f'<div>{esc(b["email"])}</div>')
    if b.get('address'): contact.append(f'<div>{esc(b["address"])}</div>')
    return f'''<footer class="footer"><div class="wrap footer-grid"><div><strong>{esc(b['name'])}</strong><p class="muted">{esc(spec.get('footer',{}).get('description',b.get('type','Business website')))}</p></div><div>{''.join(contact)}</div><div class="muted">{esc(b.get('location',''))}</div></div></footer><script src="assets/js/site.js"></script></body></html>'''

def section_html(sec, imgs):
    kind=sec.get('type','text')
    title=f'<div class="eyebrow">{esc(sec.get("eyebrow",""))}</div><h2 class="section-title">{esc(sec.get("heading",""))}</h2>'
    body=f'<p>{esc(sec.get("body",""))}</p>'
    if kind=='split':
        im=imgs.get(sec.get('_image_key',''),'')
        return f'<section><div class="wrap split"><div>{title}{body}</div><div><img src="{esc(im)}" alt="{esc(sec.get("alt",sec.get("heading","")))}"></div></div></section>'
    if kind=='cards':
        cards=''.join(f'<article class="card"><h3>{esc(c.get("title"))}</h3><p>{esc(c.get("body"))}</p></article>' for c in sec.get('cards',[]))
        return f'<section><div class="wrap">{title}{body}<div class="cards">{cards}</div></div></section>'
    if kind=='gallery':
        arr=''.join(f'<img src="{esc(imgs.get(k,""))}" alt="{esc(sec.get("heading","Gallery"))}">' for k in sec.get('_gallery_keys',[]))
        return f'<section><div class="wrap">{title}{body}<div class="gallery">{arr}</div></div></section>'
    if kind=='contact':
        items=''.join(f'<div class="contact-box"><h3>{esc(c.get("title"))}</h3><p>{esc(c.get("body"))}</p></div>' for c in sec.get('cards',[]))
        return f'<section><div class="wrap">{title}{body}<div class="contact">{items}</div></div></section>'
    return f'<section><div class="wrap">{title}<div class="intro">{body}</div></div></section>'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('--output',required=True); ap.add_argument('--self-contained',action='store_true'); a=ap.parse_args()
    spec=json.loads(Path(a.spec).read_text()); out=Path(a.output).resolve(); out.mkdir(parents=True,exist_ok=True)
    (out/'assets/css').mkdir(parents=True,exist_ok=True); (out/'assets/js').mkdir(parents=True,exist_ok=True)
    (out/'assets/css/site.css').write_text(CSS); (out/'assets/js/site.js').write_text(JS)
    imgs={}
    hero=spec.get('hero',{}); imgs['hero']=copy_img(hero.get('image'),out,'hero')
    n=0
    for page in spec.get('pages',[]):
        for sec in page.get('sections',[]):
            if sec.get('image'):
                n+=1; key=f'img{n}'; imgs[key]=copy_img(sec['image'],out,key); sec['_image_key']=key
            if sec.get('images'):
                sec['_gallery_keys']=[]
                for src in sec['images']:
                    n+=1; key=f'img{n}'; imgs[key]=copy_img(src,out,key); sec['_gallery_keys'].append(key)
    for page in spec.get('pages',[]):
        fn=page['file']; title=page.get('title',spec['business']['name']); desc=page.get('meta_description',page.get('intro',''))
        parts=[head(title,desc),nav(spec)]
        if fn=='index.html':
            parts.append(f'''<section class="hero"><img src="{esc(imgs.get('hero',''))}" alt="{esc(hero.get('alt',''))}"><div class="wrap hero-copy"><div class="eyebrow">{esc(hero.get('eyebrow',''))}</div><h1>{esc(hero.get('h1',''))}</h1><p>{esc(hero.get('body',''))}</p><a class="cta" href="{esc(hero.get('cta_href','visit.html'))}">{esc(hero.get('cta_label','Visit us'))}</a></div></section>''')
        else:
            parts.append(f'''<section class="page-hero"><div class="wrap"><div class="eyebrow">{esc(page.get('eyebrow',''))}</div><h1>{esc(page.get('h1',page.get('title','')))}</h1><p class="intro">{esc(page.get('intro',''))}</p></div></section>''')
        for sec in page.get('sections',[]): parts.append(section_html(sec,imgs))
        parts.append(footer(spec)); (out/fn).write_text(''.join(parts))
    (out/'BUILD-SPEC.json').write_text(json.dumps(spec,indent=2))
    sitemap='\n'.join(x['file'] for x in spec.get('navigation',[])); (out/'sitemap.txt').write_text(sitemap+'\n')
    if a.self_contained and (out/'index.html').exists():
        text=(out/'index.html').read_text().replace('<link rel="stylesheet" href="assets/css/site.css">',f'<style>{CSS}</style>').replace('<script src="assets/js/site.js"></script>',f'<script>{JS}</script>')
        for rel in set(imgs.values()):
            if rel:
                p=out/rel
                if p.exists(): text=text.replace(rel,data_uri(p))
        (out/'preview.html').write_text(text)
    print(out)

if __name__=='__main__': main()
