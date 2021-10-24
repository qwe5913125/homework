import datetime
import time

from flask import Flask, request

from flask_wtf import FlaskForm
from wtforms import StringField, validators


class ContactForm(FlaskForm):

    name = StringField(label='name', validators=[validators.Length(min=4, max=35)])
    email = StringField(label='E-mail', validators=[validators.Length(min=5, max=35), validators.email()])
    job = StringField(label='job', validators=[
        validators.InputRequired(),
        validators.AnyOf(values=['IT', 'Bank', 'HR'])

        ])


class BirthDayValid(FlaskForm):
    d = datetime.datetime.now()
    #print(str(d.strftime('%B')))
    x = str(d.strftime('%B'))
    print(x)

    dt = StringField(label='dt', validators=[validators.AnyOf(values=[x])])
    print(dt)



app = Flask(__name__)
#app.config['DEBUG'] = True
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return('invalid', 400)

    if request.method == 'GET':
        return 'hello world!3', 200


@app.route('/data', methods=['GET', 'POST'])
def my_data():
    if request.method == 'POST':
        form = BirthDayValid(request.form)
        print(form.validate())
        print(form.dt)

        if form.validate():
            print('Skidka3')
            return ('valid2', 200)
        else:
            print('No Skidka2')
            return('invalid2', 400)


if __name__ == '__main__':
    app.run()
