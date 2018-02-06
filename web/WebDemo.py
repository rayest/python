from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hello/userName/<userName>", methods=['GET'])
def hello_world(userName):
    return "Hello, " + userName


if __name__ == '__main__':
    app.run()
