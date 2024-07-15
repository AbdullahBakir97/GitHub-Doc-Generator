# src/parser.py
import ast
import markdown2

def parse_code_comments(file_content):
    comments = []
    tree = ast.parse(file_content)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            comment = ast.get_docstring(node)
            if comment:
                comments.append(comment)
    return comments

def parse_markdown(file_content):
    return markdown2.markdown(file_content)
