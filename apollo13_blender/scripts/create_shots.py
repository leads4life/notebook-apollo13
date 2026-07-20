from utilities import manifest,clear_scene,save_scene,add_camera,set_render,require_blender,keyframe
from build_spacecraft import build_spacecraft
from build_launch import build_launch
from build_interiors import build_interiors
from build_mission_control import build_mission_control
from build_earth_moon import build_earth_moon
from build_characters import build_characters
from build_reentry import build_reentry
from build_ocean import build_ocean
from create_lighting import light_scene
from create_compositor import configure_compositor

def build_one(shot, profile='PREVIEW'):
 bpy=require_blender();clear_scene(); kind=shot['environment']
 if kind=='launch': build_launch(); camloc=(18,-32,15);target=(0,0,42)
 elif kind=='space': build_spacecraft('VENTING' in shot['id'] or 'JETTISON' in shot['id']);build_earth_moon('space');camloc=(12,-18,7);target=(0,0,0)
 elif kind=='interior': build_interiors();build_characters();camloc=(0,-5,1.4);target=(0,1,.8)
 elif kind=='control': build_mission_control();build_characters();camloc=(7,-7,3.8);target=(0,1,.6)
 elif kind=='moon': build_spacecraft();build_earth_moon('moon');camloc=(14,-22,7);target=(0,0,0)
 elif kind=='reentry': build_reentry();build_earth_moon('reentry');camloc=(8,-14,5);target=(0,0,0)
 else: build_ocean();build_reentry();camloc=(12,-18,8);target=(0,0,0)
 cam=add_camera(shot['camera'],camloc,target,float(shot['lens'].replace('mm',''))); cam.data.dof.use_dof=False
 # Deliberate two-key camera drift; not generic handheld movement.
 cam.location=camloc;cam.keyframe_insert(data_path='location',frame=shot['frame_start']);cam.location=(camloc[0]*.94,camloc[1]*.94,camloc[2]+.35);cam.keyframe_insert(data_path='location',frame=shot['frame_end'])
 light_scene(kind);configure_compositor();s=bpy.context.scene;s.frame_start=shot['frame_start'];s.frame_end=shot['frame_end'];set_render(s,profile);s['shot_id']=shot['id'];s['lighting_assigned']=True;s['asset_dependencies']=','.join(shot['assets']);save_scene(shot['scene_file'])
def main():
 for shot in manifest()['shots']: build_one(shot)
if __name__=='__main__':main()
