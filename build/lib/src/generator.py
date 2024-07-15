# src/generator.py
import os
from jinja2 import Environment, FileSystemLoader
from src.parser import parse_code_comments, parse_markdown
from src.github_integration import fetch_repo_files

def generate_documentation(repo_name, access_token):
    files = fetch_repo_files(repo_name, access_token)
    comments = []
    markdown_content = ""

    for file in files:
        if file.path.endswith('.py'):
            content = file.decoded_content.decode()
            comments.extend(parse_code_comments(content))
        elif file.path.endswith('.md'):
            content = file.decoded_content.decode()
            markdown_content += parse_markdown(content)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')
    output = template.render(comments=comments, markdown_content=markdown_content)

    output_dir = os.path.join('docs', 'output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'documentation.html')
    with open(output_path, 'w') as f:
        f.write(output)
    return output_path  # Return the path to the generated file
