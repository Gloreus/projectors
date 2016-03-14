from flask import Flask
from flask import render_template
import data
from config import DevelopConfig


app = Flask(__name__)
app.config.from_object(DevelopConfig)


@app.route('/')
def hello_world():
    return render_template('index.html', repo = data.get_repo())


if __name__ == '__main__':
    app.run()
