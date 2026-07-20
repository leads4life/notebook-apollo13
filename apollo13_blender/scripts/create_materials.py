from utilities import require_blender

def material(name, base, metallic=0.0, rough=.5, emission=None):
    bpy=require_blender(); m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.use_nodes=True; p=m.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(*base,1); p.inputs['Metallic'].default_value=metallic; p.inputs['Roughness'].default_value=rough
    if emission: p.inputs['Emission Color'].default_value=(*emission,1); p.inputs['Emission Strength'].default_value=3
    return m
def all_materials():
    return {n:material(n,*v) for n,v in {'Painted_White':((.7,.72,.7),.75,.32),'MLI_Foil':((.5,.48,.38),.92,.23),'Anodized_Dark':((.025,.035,.05),.7,.3),'Heat_Shield':((.055,.025,.012),.15,.72),'Rubber':((.012,.012,.012),0,.78),'Panel':((.03,.05,.06),.45,.34),'CRT':((.01,.06,.035),.1,.18,(.02,.7,.25)),'Paper':((.6,.55,.43),0,.8),'Console':((.09,.16,.17),.35,.38),'Regolith':((.23,.22,.2),0,.9),'Ocean':((.008,.04,.075),.65,.18),'Parachute':((.55,.42,.27),0,.6),'Damage':((.08,.025,.01),.55,.68),'Plasma':((1,.08,.005),.1,.2,(1,.03,.001))}.items()}
