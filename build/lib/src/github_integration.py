# src/github_integration.py
from github import Github, Auth

def fetch_repo_files(repo_name, access_token):
    g = Github(auth=Auth.Token(access_token))
    repo = g.get_repo(repo_name)
    contents = repo.get_contents("")
    files = []
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            files.append(file_content)
    return files
