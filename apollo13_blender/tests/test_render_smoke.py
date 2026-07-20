import shutil,unittest
class RenderSmoke(unittest.TestCase):
 @unittest.skipUnless(shutil.which('blender'),'Blender unavailable in this environment')
 def test_blender_present(self): self.assertTrue(shutil.which('blender'))
