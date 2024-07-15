# tests/test_generator.py
import unittest
from unittest.mock import patch, MagicMock
from src.generator import generate_documentation

class TestGenerator(unittest.TestCase):
    @patch('src.generator.fetch_repo_files')
    @patch('src.generator.parse_code_comments')
    @patch('src.generator.parse_markdown')
    @patch('src.generator.Environment')
    def test_generate_documentation(self, MockEnv, mock_parse_markdown, mock_parse_code_comments, mock_fetch_repo_files):
        # Setup mocks
        mock_fetch_repo_files.return_value = [
            MagicMock(path="example.py", decoded_content=b'def foo():\n    """A function."""\n    pass'),
            MagicMock(path="README.md", decoded_content=b'# Example\nThis is a markdown file.')
        ]
        mock_parse_code_comments.return_value = ["A function."]
        mock_parse_markdown.return_value = "<h1>Example</h1><p>This is a markdown file.</p>"
        
        mock_template = MockEnv.return_value.get_template.return_value
        mock_template.render.return_value = "<html>Generated content</html>"
        
        # Test function
        repo_name = "test/repo"
        access_token = "fake_token"
        generate_documentation(repo_name, access_token)
        
        # Assertions
        mock_template.render.assert_called_once_with(
            comments=["A function."],
            markdown_content="<h1>Example</h1><p>This is a markdown file.</p>"
        )

if __name__ == '__main__':
    unittest.main()
