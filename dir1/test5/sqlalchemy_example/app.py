# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy_example.config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from sqlalchemy_example.models import Post, User, Guest
    from sqlalchemy_example.forms import PostForm

    if request.method == 'POST':
        print('1', request.form)
        form = PostForm(request.form)

        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = Post.query.all()
    #user = User.query.filter(id=posts[0].user_id)
    user = posts[0].user

    for post in posts:
        user_id = post.user_id
        user = User.query.filter_by(id=user_id).first()
        print(post.user_id, user)

        print(post.user)

    return render_template('home.txt', posts=posts)


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(username='Ivan', email='p@p.com')

    db.session.add(ivan)
    db.session.commit()  # note


def populate_db2():
    print('Creating default user')
    # Creating new ones:
    it = Guest(author='Ivan', text='test', )
    db.session.add(it)
    db.session.commit()  # note


@app.route('/create', methods=['GET', 'POST'])
def index2():
    from sqlalchemy_example.models import Post, User, Guest
    from sqlalchemy_example.forms import PostForm, GuestForm

    if request.method == 'POST':
        print('5', request.form)
        form = GuestForm(request.form)







        if form.validate():
            print('y')
            item = Guest(**form.data)
            db.session.add(item)
            db.session.commit()

            flash('Post created!')
        else:
            print('n')
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))





    items = Guest.query.all()



    return jsonify([p.to_dict() for p in items])


@app.route('/all', methods=['GET', 'POST'])
def index3():
    from sqlalchemy_example.models import Post, User, Guest
    from sqlalchemy_example.forms import PostForm, GuestForm

    if request.method == 'GET':


        items = Guest.query.all()



        return jsonify([p.to_dict() for p in items])





if __name__ == '__main__':
    from sqlalchemy_example.models import *
    db.create_all()

    if User.query.count() == 0:
        populate_db()

    if Guest.query.count() == 0:
        populate_db2()

    users = User.query.all()

    #print('1', list(map(str, users)))

    # Running app:
    app.run()
