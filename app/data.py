from git import Repo
from git import InvalidGitRepositoryError, NoSuchPathError
from flask import current_app
import os


def get_repo():
    path = current_app.config.get('REPO_ROOT', '')

    dirs = [d for d in os.scandir(path) if d.is_dir]
    res = []
    for d in dirs:
        try:
            repo = Repo(d.path)
            res.append([repo.working_dir, repo.description])
        except (InvalidGitRepositoryError, NoSuchPathError) as e:
            print(e)
    return res
