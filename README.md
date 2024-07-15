# Documentation Generator

A Python-based tool that generates comprehensive documentation from code comments and markdown files. The tool integrates with GitHub to fetch files from a repository and processes them to create a unified HTML documentation.

## Features

- Parses Python code to extract docstrings.
- Converts markdown files to HTML.
- Integrates with GitHub to fetch files from a repository.
- Uses Jinja2 templates for customizable HTML output.
- Includes a Flask web interface for easy interaction.
- Comprehensive test suite to ensure reliability.

## Requirements

- Python 3.x
- GitHub API Token
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/doc-generator.git
    cd doc-generator
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
