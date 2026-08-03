import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def run(*args): return subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,text=True,capture_output=True)
class ValidatorTests(unittest.TestCase):
    def test_passing_validation(self):
        r=run('scripts/validate_profile.py','profiles/example/profile.json'); self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        r=run('scripts/audit_html.py','examples/passing-article.html'); self.assertEqual(r.returncode,0,r.stdout+r.stderr); self.assertIn('AUDIT TOTAL: 8',r.stdout)
    def test_invalid_profile(self):
        r=run('scripts/validate_profile.py','tests/fixtures/invalid-profile.json'); self.assertEqual(r.returncode,1); self.assertIn('credential-like key',r.stdout)
    def test_forbidden_css(self):
        r=run('scripts/audit_html.py','tests/fixtures/forbidden-css.html'); self.assertEqual(r.returncode,1); self.assertIn('FAIL forbidden_css',r.stdout)
    def test_non_wechat_image_url(self):
        r=run('scripts/audit_html.py','tests/fixtures/non-wechat-image.html'); self.assertEqual(r.returncode,1); self.assertIn('FAIL image_hosts',r.stdout)
    def test_missing_takeaway(self):
        r=run('scripts/audit_html.py','tests/fixtures/missing-takeaway.html'); self.assertEqual(r.returncode,1); self.assertIn('FAIL takeaway',r.stdout)
    def test_sensitive_local_path_and_secret_detection(self):
        r=run('scripts/audit_html.py','tests/fixtures/sensitive-local.html'); self.assertEqual(r.returncode,1); self.assertIn('FAIL sensitive_content',r.stdout)
    def test_build_excludes_private_material(self):
        gitignore = (ROOT/'.gitignore').read_text(encoding='utf-8')
        self.assertIn('private/', gitignore)
        self.assertIn('.env', gitignore)
    def test_no_image_no_offer_passes(self):
        r=run('scripts/audit_html.py','tests/fixtures/no-image-no-offer.html'); self.assertEqual(r.returncode,0,r.stdout+r.stderr); self.assertIn('PASS image_hosts',r.stdout)

if __name__=='__main__': unittest.main()
