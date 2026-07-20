from utilities import require_blender
from create_materials import all_materials
def build_characters():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_Characters');bpy.context.scene.collection.children.link(c)
 for i in range(3):
  x=-1.2+i*1.2
  bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,radius=.28,location=(x,.2,1.6));o=bpy.context.object;o.name='Helmeted_Astronaut_%02d'%i;o.data.materials.append(m['Anodized_Dark'])
  bpy.ops.mesh.primitive_cylinder_add(vertices=12,radius=.32,depth=1.1,location=(x,.2,.85));o=bpy.context.object;o.name='Astronaut_Suit_%02d'%i;o.data.materials.append(m['Painted_White'])
 return c
