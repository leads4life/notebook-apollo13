"""Frame integrity, contact-sheet and basic luma QC for resumable renders."""
from __future__ import annotations
import argparse, json
from utilities import manifest,path
def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',default='PREVIEW');a=p.parse_args();m=manifest();missing=[];tiny=[];frames=[]
 for s in m['shots']:
  for f in range(s['frame_start'],s['frame_end']+1):
   q=path('frames',a.profile,s['id'],f'frame_{f:04d}.png')
   if not q.exists():missing.append(str(q))
   elif q.stat().st_size<1024:tiny.append(str(q))
   else:frames.append(q)
 report={'profile':a.profile,'expected':m['project_settings']['total_frames'],'present':len(frames),'missing':missing,'tiny':tiny,'black_frame_candidates':[],'overexposure_candidates':[],'duplicate_frame_candidates':[]}
 try:
  from PIL import Image,ImageDraw
  thumbs=[]
  for q in frames[::max(1,len(frames)//28)][:28]:
   im=Image.open(q).convert('RGB'); px=list(im.resize((32,18)).getdata()); mean=sum(sum(v) for v in px)/(len(px)*3); report['black_frame_candidates'] += [str(q)] if mean<3 else [];report['overexposure_candidates'] += [str(q)] if mean>248 else []; thumbs.append((q,im.copy()))
  if thumbs:
   sheet=Image.new('RGB',(640,((len(thumbs)+3)//4)*110),(8,8,10));d=ImageDraw.Draw(sheet)
   for i,(q,im) in enumerate(thumbs):
    im.thumbnail((150,85));x=(i%4)*160;y=(i//4)*110;sheet.paste(im,(x,y));d.text((x,y+88),q.parent.name+' '+q.stem,fill='white')
   sheet.save(path('previews',f'{a.profile.lower()}_contact_sheet.png'))
 except ImportError: report['image_analysis']='Pillow unavailable; existence/size checks only.'
 path('logs',f'{a.profile.lower()}_qc.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));return not missing and not tiny
if __name__=='__main__':raise SystemExit(0 if main() else 1)
