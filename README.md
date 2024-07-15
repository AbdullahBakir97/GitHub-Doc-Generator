# Documentation Generator

A Python-based tool that generates comprehensive documentation from code comments and markdown files. The tool integrates with GitHub to fetch files from a repository and processes them to create a unified HTML documentation.

## Features

- **Code Comment Parsing:** Extracts docstrings from Python code.
- **Markdown Conversion:** Converts markdown files to HTML.
- **GitHub Integration:** Fetches files from GitHub repositories.
- **Customizable Templates:** Uses Jinja2 templates for HTML output.
- **Web Interface:** Provides a Flask-based web interface.
- **Comprehensive Testing:** Includes a full test suite.

## Requirements

- Python 3.x
- GitHub API Token
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdullahBakir97/GitHub-Doc-Generator.git
    cd GitHub-Doc-Generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Command Line
Run the generator script with your GitHub repository name and access token:
```bash
python src/generator.py
```
### Web Interface
Start the Flask app:
```bash
python src/app.py
```
Access the web interface at `http://127.0.0.1:5000/generate_docs` and provide your repository name and access token to generate documentation.

## Testing
Run the test suite to ensure everything works correctly:
```bash
python -m unittest discover tests
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

## License
This project is licensed under the MIT License.


