from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import os


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class SharedNote():
    note = db.relationship('Note')
    destinatario = db.Column(db.Integer, db.ForeignKey('user.id'))

class Friendship():
    user = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class ImageNote:
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(10000))
     date = db.Column(db.DateTime(timezone=True), default=func.now())
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Group():
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class GroupUser():
    usuario = db.relationship('User')
    group = db.relationship('Group')