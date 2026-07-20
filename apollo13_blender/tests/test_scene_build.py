import pathlib,shutil,subprocess,unittest
class SceneBuild(unittest.TestCase):
 @unittest.skipUnless(shutil.which('blender'),'Blender unavailable in this environment')
 def test_build_assets_headless(self):
  r=pathlib.Path(__file__).parents[1];subprocess.run(['blender','--background','--python',str(r/'scripts/build_assets.py')],cwd=r,check=True);self.assertTrue((r/'assets/generated/apollo13_assets.blend').exists())
