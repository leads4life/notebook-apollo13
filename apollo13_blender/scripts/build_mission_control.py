from utilities import require_blender,add_bevel
from create_materials import all_materials
def build_mission_control():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_MissionControl');bpy.context.scene.collection.children.link(c)
 def cube(n,s,l,mat):
  bpy.ops.mesh.primitive_cube_add(location=l);o=bpy.context.object;o.name=n;o.scale=s;o.data.materials.append(mat);add_bevel(o,.02);return o
 for row in range(3):
  for col in range(6):
   x=(col-2.5)*1.35;y=row*1.5;cube('Console_%s_%s'%(row,col),(.55,.42,.3),(x,y,0),m['Console']);cube('CRT_%s_%s'%(row,col),(.32,.03,.2),(x,y-.25,.55),m['CRT'])
 cube('Status_Board',(4,.06,1.3),(0,4,2),m['Panel']);return c
