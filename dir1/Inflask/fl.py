from flask import Flask
import os

from pathlib import Path

app = Flask(__name__)
@app.route('/hello/<user>')
def home(user):
    return 'Hello user!' + user

@app.route('/sum2/<x>_<y>')
def sum2(x, y):



    return str(int(x) + int(y))


@app.route('/increased/<x>_<y>_<z>')
def incteased(x, y, z):

    pre_rezult = max(x, y, key=len)
    r = max(pre_rezult, z, key=len)


@app.route('/op/<path>')
def op(path):

    r = os.path.exists(path)



    return str(r)


app.run()
