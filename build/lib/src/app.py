# src/app.py
import sys
import os
import logging
from flask import Flask, request, send_file, jsonify
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.generator import generate_documentation

app = Flask(__name__)

@app.route('/generate_docs', methods=['POST'])
def generate_docs():
    try:
        repo_name = request.form['repo']
        access_token = request.form['access_token']
        output_path = generate_documentation(repo_name, access_token)
        if os.path.exists(output_path):
            return send_file(output_path)
        else:
            raise FileNotFoundError(f"File not found: {output_path}")
    except Exception as e:
        app.logger.error(f"Error generating documentation: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
