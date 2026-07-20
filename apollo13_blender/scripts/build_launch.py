from utilities import require_blender,add_bevel
from create_materials import all_materials
def build_launch():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_Launch');bpy.context.scene.collection.children.link(c)
 def cube(n,scale,loc,mat):
  bpy.ops.mesh.primitive_cube_add(location=loc);o=bpy.context.object;o.name=n;o.scale=scale;o.data.materials.append(mat);add_bevel(o,.05);return o
 bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=1.7,depth=105,location=(0,0,52.5)); r=bpy.context.object;r.name='Saturn_V';r.data.materials.append(m['Painted_White'])
 for x in (-9,9):
  for z in range(10,100,15):cube('Tower_Truss',(0.25,0.25,8),(x,0,z),m['Anodized_Dark'])
 cube('Launch_Pad',(15,15,.5),(0,0,0),m['Console']);return c
