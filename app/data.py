from git import Repo
from git import InvalidGitRepositoryError, NoSuchPathError
from flask import current_app
import os
import time


def get_repo():
    path = current_app.config.get('REPO_ROOT', '')

    dirs = [(os.path.join(path, d), d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    res = []
    for p, f in dirs:
        try:
            repo = Repo(p)
            rep_info = {}
            if repo.refs:
                try:
                    commit = repo.commit()
                    rep_info["author"] = commit.author
                    rep_info["date"] = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime(commit.committed_date))
                except ValueError:
                    pass
            rep_info["name"] = f
            rep_info["desc"] = repo.description

            res.append(rep_info)
        except (InvalidGitRepositoryError, NoSuchPathError) as e:
            print(e)
    return res
