from utilities import require_blender
from create_materials import all_materials
def build_ocean():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_Ocean');bpy.context.scene.collection.children.link(c)
 bpy.ops.mesh.primitive_plane_add(size=300,location=(0,0,-2));o=bpy.context.object;o.name='South_Pacific_Ocean';o.data.materials.append(m['Ocean'])
 for i in range(3):
  bpy.ops.mesh.primitive_cone_add(vertices=24,radius1=2.1,radius2=.12,depth=4,location=((i-1)*4,0,7));o=bpy.context.object;o.name='Parachute_%02d'%i;o.data.materials.append(m['Parachute'])
 return c
