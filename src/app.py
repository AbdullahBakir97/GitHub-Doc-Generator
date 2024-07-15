# src/app.py
from flask import Flask, request, send_file
from src.generator import generate_documentation

app = Flask(__name__)

@app.route('/generate_docs', methods=['POST'])
def generate_docs():
    repo_name = request.form['repo']
    access_token = request.form['access_token']
    generate_documentation(repo_name, access_token)
    return send_file('docs/output/documentation.html')

if __name__ == '__main__':
    app.run(debug=True)
