import pathlib,unittest
class Layout(unittest.TestCase):
 def test_required_scripts(self):
  root=pathlib.Path(__file__).parents[1]; names=['build_all.py','build_assets.py','create_shots.py','render_all.py','assemble_video.py','validate_project.py'];self.assertTrue(all((root/'scripts'/n).exists() for n in names))
