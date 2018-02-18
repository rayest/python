from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(Form):
    username = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    username = 'lee'
    name_form = NameForm()
    if name_form.validate_on_submit():
        session['username'] = name_form.username.data
        name_form.username.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=name_form, username=session.get('username'))


if __name__ == '__main__':
    app.run(debug=True)
