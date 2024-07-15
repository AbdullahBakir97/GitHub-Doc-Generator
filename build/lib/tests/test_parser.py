# tests/test_parser.py
import unittest
from src.parser import parse_code_comments, parse_markdown

class TestParser(unittest.TestCase):
    def test_parse_code_comments(self):
        content = """
def example_function():
    \"\"\"This is a docstring.\"\"\"
    pass
"""
        comments = parse_code_comments(content)
        self.assertEqual(comments, ["This is a docstring."])

    def test_parse_markdown(self):
        content = "# Example\nThis is a markdown file."
        html_content = parse_markdown(content)
        self.assertIn('<h1>Example</h1>', html_content)
        self.assertIn('<p>This is a markdown file.</p>', html_content)

if __name__ == '__main__':
    unittest.main()
