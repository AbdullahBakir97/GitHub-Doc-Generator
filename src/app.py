# src/app.py

import os
from flask import Flask, request, send_file
from dotenv import load_dotenv
from src.generator import generate_documentation

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/generate_docs', methods=['POST'])
def generate_docs():
    repo_name = request.form.get('repo')
    if not repo_name:
        return 'Error: Missing required parameter "repo"', 400
    
    access_token = os.getenv('GITHUB_TOKEN')
    generate_documentation(repo_name, access_token)
    return send_file('docs/output/documentation.html')

    

if __name__ == '__main__':
    app.run(debug=True)
