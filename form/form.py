from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    username = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    username = 'lee'
    name_form = NameForm()
    if name_form.validate_on_submit():
        username = name_form.username.data
        name_form.username.data = ''
    return render_template('index.html', form=name_form, username=username)


if __name__ == '__main__':
    app.run(debug=True)
