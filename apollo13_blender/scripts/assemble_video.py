from __future__ import annotations
import argparse,subprocess,shutil
from utilities import manifest,path
def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',default='FINAL');p.add_argument('--output',default=None);a=p.parse_args();m=manifest(); lst=path('logs',f'{a.profile.lower()}_concat.txt');lst.parent.mkdir(exist_ok=True)
 lines=[]
 for s in m['shots']:
  d=path('frames',a.profile,s['id'])
  for f in range(s['frame_start'],s['frame_end']+1):
   image=d/f'frame_{f:04d}.png'
   if not image.exists():raise SystemExit(f'Missing frame: {image}')
   lines.append("file '"+str(image.resolve())+"'")
 lst.write_text('\n'.join(lines)+'\n');out=path(a.output) if a.output else path('output','apollo13_the_long_way_home.mp4');out.parent.mkdir(exist_ok=True)
 ff=shutil.which('ffmpeg')
 if not ff:raise SystemExit('ffmpeg not found')
 subprocess.run([ff,'-y','-r','24','-f','concat','-safe','0','-i',str(lst),'-i',str(path('audio/procedural_score.wav')),'-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest',str(out)],check=True)
if __name__=='__main__':main()
