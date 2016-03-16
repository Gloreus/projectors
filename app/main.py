from flask import Flask
from flask import render_template
import data
from config import DevelopConfig


app = Flask(__name__)
app.config.from_object(DevelopConfig)


@app.route('/')
def hello_world():
    return render_template('index.html', repo=data.get_repo_list())


@app.route('/repo/<string:reponame>')
def repo(reponame):
    return render_template('repo.html', reponame=reponame, rep_info=data.get_repo_info(reponame))


if __name__ == '__main__':
    app.run()
