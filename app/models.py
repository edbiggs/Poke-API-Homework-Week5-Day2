from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    team = db.relationship("Team", backref="owner")

    # def __init__(self, username, password, email):
    #     self.username = username
    #     self.password = password
    #     self.email = email


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name =  db.Column(db.String(100),nullable=False)
    ability =  db.Column(db.String(100),nullable=False)
    base_hp =  db.Column(db.Integer, nullable=False)
    base_att =  db.Column(db.Integer, nullable=False)
    base_def =  db.Column(db.Integer, nullable=False)
    sprite_url =  db.Column(db.String, nullable=False)


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name =  db.Column(db.String(100),nullable=False)
    ability =  db.Column(db.String(100),nullable=False)
    base_hp =  db.Column(db.Integer, nullable=False)
    base_att =  db.Column(db.Integer, nullable=False)
    base_def =  db.Column(db.Integer, nullable=False)
    sprite_url =  db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

