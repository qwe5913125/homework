# -*- coding: utf-8 -*-

from datetime import date

from sqlalchemy_example.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __str__(self):
        return '<User %r id - %s>' % (self.username, self.id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
        index=True
    )
    user = db.relationship(User, foreign_keys=[user_id, ])

    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)

    def __str__(self):
        return '<Post %r, user_id %s>'.format(self.title, self.user_id)


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(5))
    text = db.Column(db.String(50000), nullable=False)
    datetimecreate = db.Column(db.Date, default=date.today)
    si_visible = db.Column(db.Boolean, default=True, nullable=False)


    def to_dict(self):
        return {
            'author': self.author,
            'text': self.text,
            'datetimecreate': self.datetimecreate
        }




    def __str__(self):
        return '<User %r id - %s>' % (self.username, self.id)


