# tests/test_github_integration.py
import unittest
from unittest.mock import patch
from src.github_integration import fetch_repo_files

class TestGitHubIntegration(unittest.TestCase):
    @patch('src.github_integration.Github')
    def test_fetch_repo_files(self, MockGithub):
        # Setup mock
        instance = MockGithub.return_value
        instance.get_repo.return_value.get_contents.return_value = [
            MockGithub.return_value.get_repo.return_value.get_contents.return_value
        ]
        
        # Test function
        repo_name = "test/repo"
        access_token = "fake_token"
        files = fetch_repo_files(repo_name, access_token)
        
        # Assertions
        self.assertIsInstance(files, list)
        self.assertGreater(len(files), 0)

if __name__ == '__main__':
    unittest.main()
