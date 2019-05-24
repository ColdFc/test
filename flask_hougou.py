from flask import Flask
from flask import request

app = Flask(__name__, static_url_path="", static_folder="static")


class Config(object):
    DEBUG = True


app.config.from_object(Config)


@app.route("/", methods=["GET"])
def index():
    with open("templates/home.html", "rb") as f:
        content = f.read()
    return content


@app.route("/login.html", methods=["GET", "POST"])
def login():
    with open("templates/login.html", "rb") as f:
        content = f.read()
    return content


@app.route("/register.html", methods=["POST", "GET"])
def register():
    with open("templates/register.html", "rb") as f:
        content = f.read()
    return content


if __name__ == '__main__':
    app.run(debug=True)
