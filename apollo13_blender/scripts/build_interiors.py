from utilities import require_blender,add_bevel
from create_materials import all_materials
def build_interiors():
 bpy=require_blender();m=all_materials();c=bpy.data.collections.new('ASSET_Interior');bpy.context.scene.collection.children.link(c)
 def cube(n,s,l,mat):
  bpy.ops.mesh.primitive_cube_add(location=l);o=bpy.context.object;o.name=n;o.scale=s;o.data.materials.append(mat);add_bevel(o,.02);return o
 cube('Cabin_Backwall',(4,.15,2.5),(0,2,0),m['Panel']);cube('Instrument_Panel',(3,.15,1.3),(0,1.7,.8),m['Panel'])
 for i in range(12):cube('Instrument_CRT_%02d'%i,(0.28,.03,.2),(-2.2+(i%6)*.85,1.51,.8+(i//6)*.55),m['CRT'])
 cube('Floating_Checklist',(0.35,.01,.48),(.8,.4,.4),m['Paper']);return c
