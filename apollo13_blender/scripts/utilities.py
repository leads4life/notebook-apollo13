"""Shared deterministic utilities; works in CPython and Blender's Python."""
from __future__ import annotations
import json, os, pathlib, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def path(*parts): return ROOT.joinpath(*parts)
def load_json(name): return json.loads(path(name).read_text())
def manifest(): return load_json('production_manifest.json')
def ensure_dirs():
    for p in ('scenes','assets/generated','assets/cache','audio','frames','previews','output','logs'): path(p).mkdir(parents=True,exist_ok=True)
def blender_available(): return bool(os.environ.get('BLENDER_EXECUTABLE') or __import__('shutil').which('blender'))
def run(cmd, **kwargs): return subprocess.run(cmd, check=True, text=True, **kwargs)
def require_blender():
    try: import bpy; return bpy
    except ImportError as exc: raise RuntimeError('Run this script with blender --background --python') from exc
def clear_scene():
    bpy=require_blender(); bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.materials, bpy.data.meshes, bpy.data.curves, bpy.data.cameras, bpy.data.lights):
        for item in list(datablocks):
            if item.users == 0: datablocks.remove(item)
def set_render(scene, profile='PREVIEW'):
    cfg=load_json('render_config.json')[profile]; scene.render.resolution_x,scene.render.resolution_y=cfg['resolution']; scene.render.resolution_percentage=100; scene.render.fps=24
    scene.render.image_settings.file_format='PNG'; scene.render.image_settings.color_mode='RGBA'; scene.render.film_transparent=False
    scene.render.engine=cfg['engine'] if cfg['engine'] in {'BLENDER_EEVEE_NEXT','CYCLES'} else 'BLENDER_EEVEE_NEXT'
    if scene.render.engine=='CYCLES': scene.cycles.samples=cfg['samples']; scene.cycles.use_denoising=cfg.get('denoise',False); scene.cycles.use_adaptive_sampling=True
    scene.render.use_file_extension=True
def save_scene(filename):
    bpy=require_blender(); ensure_dirs(); bpy.ops.wm.save_as_mainfile(filepath=str(path(filename)))
def add_bevel(obj, width=.03):
    mod=obj.modifiers.new('VisibleEdgeBevel','BEVEL'); mod.width=width; mod.segments=2
    return obj
def look_at(obj, target):
    import mathutils; obj.rotation_euler=(mathutils.Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()
def add_camera(name, loc, target, lens=50):
    bpy=require_blender(); bpy.ops.object.camera_add(location=loc); o=bpy.context.object; o.name=name; o.data.lens=lens; o.data.sensor_width=36; look_at(o,target); bpy.context.scene.camera=o; return o
def add_sun(energy=3, angle=.08):
    bpy=require_blender(); bpy.ops.object.light_add(type='SUN', location=(0,0,10)); o=bpy.context.object; o.name='SUN_Key'; o.data.energy=energy; o.data.angle=angle; o.rotation_euler=(.5,-.3,-.6); return o
def keyframe(obj, prop, frame, value): setattr(obj,prop,value); obj.keyframe_insert(data_path=prop,frame=frame)
