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

    os.makedirs('docs/output', exist_ok=True)
    with open('docs/output/documentation.html', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    repo_name = "username/repo"
    access_token = "your_access_token"
    generate_documentation(repo_name, access_token)
