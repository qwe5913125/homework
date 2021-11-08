import datetime
import time
import os
import random

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

class IntValid(FlaskForm):
    e = StringField(label='E', validators=[validators.NumberRange(1, 30)])
    print('E ravno======', e)



app = Flask(__name__)
#app.config['DEBUG'] = True
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret',
    WTF_CSRF_ENABLED=False,
)

random.seed(os.environ['S'])

x1 = 0
def get_in():
    global x1
    x1 = random.randint(1, 30)
    return True


@app.route('/', methods=['GET', 'POST'])
def home():
    print('!!!!!!!!!!!!!!!!')
    get_in()
    global x1
    print('1', x1)
    return 'Число загадано!', 200



@app.route('/guess', methods=['POST'])
def my_guest():
    if request.method == 'POST':
        er =list(request.form.values())
        print(er[0])
        global x1

        if (str(x1) == er[0]):
            print("DA!!!!!!!!!!!")
        else:
            print('Net!!!')

    return('test2', 200)



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
