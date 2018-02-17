from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<user_name>')
def user(user_name):
    return render_template('user.html', userName=user_name)


if __name__ == '__main__':
    app.run()
