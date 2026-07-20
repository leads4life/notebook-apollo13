from utilities import require_blender
from create_materials import all_materials
def build_earth_moon(kind='space'):
 bpy=require_blender();m=all_materials(); c=bpy.data.collections.new('ASSET_Celestial');bpy.context.scene.collection.children.link(c)
 def sphere(n,r,loc,mat):
  bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24,radius=r,location=loc);o=bpy.context.object;o.name=n;o.data.materials.append(mat);return o
 if kind in ('space','moon','reentry'): sphere('Earth',18,(40,0,0),m['Ocean'])
 if kind=='moon': sphere('Moon',32,(0,-42,-7),m['Regolith'])
 # deterministic stars as world points are cheaper than geometry
 bpy.context.scene.world.color=(.0003,.0005,.001)
 return c
