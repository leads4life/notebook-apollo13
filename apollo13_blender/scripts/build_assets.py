from utilities import clear_scene,save_scene,require_blender
from build_spacecraft import build_spacecraft
from build_launch import build_launch
from build_interiors import build_interiors
from build_mission_control import build_mission_control
from build_earth_moon import build_earth_moon
from build_characters import build_characters
from build_reentry import build_reentry
from build_ocean import build_ocean
def main():
 clear_scene();build_spacecraft(True);build_launch();build_interiors();build_mission_control();build_earth_moon('moon');build_characters();build_reentry();build_ocean();save_scene('assets/generated/apollo13_assets.blend')
if __name__=='__main__':main()
