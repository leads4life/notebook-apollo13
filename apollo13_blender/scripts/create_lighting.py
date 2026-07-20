from utilities import require_blender,add_sun
def light_scene(kind):
 bpy=require_blender(); s=bpy.context.scene; s.world.color=(.002,.003,.006) if kind not in ('launch','ocean') else (.05,.08,.12); add_sun(3 if kind!='interior' else .5)
 if kind in ('interior','control'):
  for x in (-2,0,2):
   bpy.ops.object.light_add(type='AREA',location=(x,0,3));o=bpy.context.object;o.name='Practical_%s'%x;o.data.energy=250;o.data.shape='RECTANGLE';o.data.color=(.55,.75,1) if kind=='interior' else (1,.65,.35);o.data.size=2
 if kind=='reentry':
  bpy.ops.object.light_add(type='POINT',location=(0,-3,0));o=bpy.context.object;o.name='Plasma_Rim';o.data.energy=900;o.data.color=(1,.06,.005)
