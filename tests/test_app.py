# tests/test_app.py
import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_docs(self):
        response = self.app.post('/generate_docs', data=dict(
            repo="test/repo",
            access_token="fake_token"
        ))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
