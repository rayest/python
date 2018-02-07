from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hello/userName/<user_name>", methods=['GET'])
def hello_world(user_name):
    return "Hello, " + user_name


if __name__ == '__main__':
    app.run()
