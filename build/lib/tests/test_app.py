# tests/test_app.py
import unittest
from unittest.mock import patch
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('src.app.generate_documentation')
    @patch('os.path.exists')
    @patch('flask.send_file')
    def test_generate_docs(self, mock_send_file, mock_exists, mock_generate_documentation):
        mock_generate_documentation.return_value = 'docs/output/documentation.html'
        mock_exists.return_value = True
        mock_send_file.return_value = 'Mocked File Response'
        
        response = self.app.post('/generate_docs', data=dict(
            repo="test/repo",
            access_token="fake_token"
        ))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

