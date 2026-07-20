from __future__ import annotations
import argparse,subprocess,shutil
from utilities import manifest,path

def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',default='PREVIEW');p.add_argument('--shot');p.add_argument('--retries',type=int,default=1);p.add_argument('--start',type=int);p.add_argument('--end',type=int);a=p.parse_args(); blender=shutil.which('blender') or __import__('os').environ.get('BLENDER_EXECUTABLE')
 if not blender:raise SystemExit('Blender executable unavailable; set BLENDER_EXECUTABLE.')
 shots=[s for s in manifest()['shots'] if not a.shot or s['id']==a.shot]
 for s in shots:
  cmd=[blender,'--background',str(path(s['scene_file'])),'--python',str(path('scripts/render_shot.py')),'--','--shot',s['id'],'--profile',a.profile]+(['--start',str(a.start)] if a.start else [])+(['--end',str(a.end)] if a.end else [])
  subprocess.run(cmd,check=True)
if __name__=='__main__':main()
