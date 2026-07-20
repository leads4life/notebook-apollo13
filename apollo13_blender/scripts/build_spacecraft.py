from utilities import require_blender,add_bevel
from create_materials import all_materials
def cyl(name,r,depth,loc,mat,rot=(0,0,0)):
 bpy=require_blender(); bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=depth,location=loc,rotation=rot); o=bpy.context.object;o.name=name;o.data.materials.append(mat);add_bevel(o,.025);return o
def build_spacecraft(damaged=False):
 bpy=require_blender(); m=all_materials(); c=bpy.data.collections.new('ASSET_Spacecraft');bpy.context.scene.collection.children.link(c)
 def move(o):
  for cc in list(o.users_collection):cc.objects.unlink(o)
  c.objects.link(o);return o
 # longitudinal X axis
 move(cyl('Odyssey_Command_Module',1.45,1.8,(0,0,0),m['Painted_White'],(0,1.5708,0)))
 move(cyl('Service_Module',1.35,5.4,(-3.3,0,0),m['MLI_Foil'],(0,1.5708,0)))
 for y,z in [(1.25,0),(-1.25,0),(0,1.25),(0,-1.25)]:move(cyl('RCS_Pod',.22,.7,(-.5,y,z),m['Anodized_Dark'],(0,1.5708,0)))
 move(cyl('Aquarius_Lunar_Module',1.15,2.0,(2.2,0,0),m['MLI_Foil'],(0,1.5708,0)))
 if damaged:
  panel=move(cyl('Damaged_Service_Panel',.52,.04,(-3.32,-1.3,.15),m['Damage'],(0,1.5708,0))); panel.rotation_euler[1]=1.2
 return c
