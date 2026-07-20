from utilities import require_blender
def configure_compositor():
 bpy=require_blender();s=bpy.context.scene;s.use_nodes=True;n=s.node_tree;n.nodes.clear();rl=n.nodes.new('CompositorNodeRLayers');gl=n.nodes.new('CompositorNodeGlare');gl.glare_type='FOG_GLOW';gl.quality='HIGH';gl.threshold=1.5;gl.size=6;comp=n.nodes.new('CompositorNodeComposite');n.links.new(rl.outputs['Image'],gl.inputs['Image']);n.links.new(gl.outputs['Image'],comp.inputs['Image'])
 # Scene-referred defaults are version-safe; AgX exists in Blender 4+.
 try:s.view_settings.look='AgX - Medium High Contrast'
 except Exception:pass
