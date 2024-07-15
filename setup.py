from setuptools import setup, find_packages

setup(
    name='doc-generator',
    version='1.0.0',
    description='A tool to generate documentation from code comments and markdown files.',
    author='@AbdullahBakir97',
    author_email='abdullah.bakir.204@gmail.com',
    url='https://github.com/AbdullahBakir97/GitHub-Doc-Generator',
    packages=find_packages(),
    install_requires=[
        'flask',
        'jinja2',
        'markdown2',
        'PyGithub',
    ],
    entry_points={
        'console_scripts': [
            'doc-generator=src.generator:generate_documentation',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)