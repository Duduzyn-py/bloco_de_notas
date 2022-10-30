from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import os


"""
Tabea para Amigos

friends = db.Table('friends',
db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
db.Column('friend_id', db.Integer, db.ForeignKey('user.id'))
)
"""
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
    
"""    
    friends = db.relationship('User', #defining the relationship, User is left side entity
        secondary = friends, 
        primaryjoin = (friends.c.user_id == id), 
        secondaryjoin = (friends.c.friend_id == id),
        lazy = 'dynamic'
    )

    def add_friend(self, user):
        if not self.is_friend(user):
            self.friends.append(user)
            return self

    def remove_friend(self, user):
        if self.is_friend(user):
            self.friends.remove(user)
            return self

    def is_friend(self, user):
        return self.friends.filter(friends.c.friend_id == user.id).count() > 0
"""

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