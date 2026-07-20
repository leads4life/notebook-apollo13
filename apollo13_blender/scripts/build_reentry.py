from utilities import require_blender
from create_materials import all_materials
def build_reentry():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_Reentry');bpy.context.scene.collection.children.link(c)
 bpy.ops.mesh.primitive_cone_add(vertices=48,radius1=1.7,radius2=1.15,depth=1.8,location=(0,0,0));o=bpy.context.object;o.name='Command_Module_Reentry';o.data.materials.append(m['Heat_Shield'])
 bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=2.05,location=(0,0,0));o=bpy.context.object;o.name='Procedural_Plasma_Envelope';o.scale=(1,1,.7);o.data.materials.append(m['Plasma']);return c
