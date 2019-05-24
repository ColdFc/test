from flask import Flask

app = Flask(__name__)


@app.route("/register")
def index():
    return "我卢本伟没有开挂"


if __name__ == '__main__':
    app.run(debug=True)
