import json,pathlib,unittest
class FrameRanges(unittest.TestCase):
 def test_contiguous(self):
  s=json.loads((pathlib.Path(__file__).parents[1]/'production_manifest.json').read_text())['shots'];self.assertEqual(1,s[0]['frame_start']);self.assertTrue(all(a['frame_end']+1==b['frame_start'] for a,b in zip(s,s[1:])))
