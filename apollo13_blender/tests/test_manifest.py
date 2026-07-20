import json,pathlib,unittest
ROOT=pathlib.Path(__file__).parents[1]
class ManifestTests(unittest.TestCase):
 def test_schema_basics(self):
  m=json.loads((ROOT/'production_manifest.json').read_text());self.assertEqual(28,len(m['shots']));self.assertEqual(24,m['project_settings']['fps']);self.assertEqual(1800,m['project_settings']['total_frames'])
