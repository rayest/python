# coding=utf-8
from flask import Flask, jsonify, make_response

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
users = [
    {
        'id': 1,
        'username': '李雷',
        'description': '我是李雷'
    },
    {
        'id': 2,
        'username': '韩梅梅',
        'description': '我是韩梅梅'
    }
]


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify({'error': "Not found"})), 404


if __name__ == '__main__':
    app.run()
