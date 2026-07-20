from __future__ import annotations
import argparse,json,pathlib,shutil,sys
from utilities import path,manifest,load_json,ensure_dirs
def check(condition,message,errors):
 if not condition:errors.append(message)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--after-build',action='store_true');a=ap.parse_args();ensure_dirs(); errors=[];m=manifest();settings=m['project_settings'];shots=m['shots'];check(settings['fps']==24,'fps must be 24',errors);check(settings['final_resolution']==[1920,1080],'final resolution mismatch',errors);check(1800<=settings['total_frames']<=2160,'frame count outside target',errors);check(len({s['id'] for s in shots})==len(shots),'duplicate shot IDs',errors)
 last=0
 for s in shots:
  check(s['frame_start']==last+1,f"frame gap/overlap at {s['id']}",errors);check(s['frame_end']>=s['frame_start'],f"invalid range {s['id']}",errors);last=s['frame_end'];check(bool(s['camera']),f"missing camera {s['id']}",errors);check(bool(s['lighting_motivation']),f"missing lighting {s['id']}",errors)
  if a.after_build:check(path(s['scene_file']).exists(),f"scene not built: {s['scene_file']}",errors)
 check(last==settings['total_frames'],'manifest total does not match ranges',errors);check(path('render_config.json').exists(),'missing render config',errors);check(path('audio').is_dir(),'audio directory missing',errors);check(os_access(path('frames')),'frame output not writable',errors);
 if shutil.which('ffmpeg') is None: print('WARNING: ffmpeg unavailable; assembly runtime test pending.')
 report={'ok':not errors,'shots':len(shots),'frames':last,'errors':errors};path('logs/validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));return not errors
def os_access(p):
 try:
  p.mkdir(parents=True,exist_ok=True);probe=p/'.write_probe';probe.write_text('ok');probe.unlink();return True
 except OSError:return False
if __name__=='__main__':sys.exit(0 if main() else 1)
