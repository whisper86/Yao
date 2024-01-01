from flask import Flask

app = Flask(__name__)


@app.route("/")
def func():
    return "xuyao & yiyi"


if __name__ == '__main__':
    app.run()

func()
