from __future__ import annotations
import argparse,pathlib,sys
from utilities import manifest,path,load_json,require_blender,set_render

def completed(p): return p.exists() and p.stat().st_size>1024
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--shot',required=True);ap.add_argument('--profile',default='PREVIEW');ap.add_argument('--start',type=int);ap.add_argument('--end',type=int);ap.add_argument('--retry',action='store_true');a=ap.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else None)
 shot=next((x for x in manifest()['shots'] if x['id']==a.shot),None)
 if not shot:raise SystemExit('Unknown shot '+a.shot)
 bpy=require_blender(); scene=bpy.context.scene;set_render(scene,a.profile);out=path('frames',a.profile,shot['id']);out.mkdir(parents=True,exist_ok=True);start=a.start or shot['frame_start'];end=a.end or shot['frame_end'];scene.render.filepath=str(out/'frame_')
 for f in range(start,end+1):
  target=out/f'frame_{f:04d}.png'
  if completed(target) and not a.retry:continue
  scene.frame_set(f);scene.render.filepath=str(out/f'frame_{f:04d}');bpy.ops.render.render(write_still=True)
if __name__=='__main__':main()
