"""Creates deterministic original tonal-bed placeholder audio; no external samples."""
import math,wave,struct
from utilities import path,manifest
def main():
 rate=48000; seconds=manifest()['project_settings']['duration_seconds']; out=path('audio/procedural_score.wav');out.parent.mkdir(exist_ok=True)
 with wave.open(str(out),'w') as w:
  w.setparams((1,2,rate,0,'NONE','not compressed'))
  for i in range(int(rate*seconds)):
   t=i/rate; envelope=.12 if t<12 else .035; x=envelope*(math.sin(2*math.pi*48*t)+.35*math.sin(2*math.pi*71*t)+.12*math.sin(2*math.pi*220*t));w.writeframesraw(struct.pack('<h',max(-32767,min(32767,int(x*32767)))))
if __name__=='__main__':main()
