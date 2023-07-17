from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

team = db.Table("team",
   db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
   db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id")))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    team = db.relationship("Pokemon", backref="team", secondary=team, lazy="dynamic")

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def catch(self, pokemon):
        self.team.append(pokemon)
        db.session.commit()

    def release_poke(self, pokemon):
        self.team.remove(pokemon)
        db.session.commit()



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name =  db.Column(db.String(100),nullable=False)
    ability =  db.Column(db.String(100),nullable=False)
    base_hp =  db.Column(db.Integer, nullable=False)
    base_att =  db.Column(db.Integer, nullable=False)
    base_def =  db.Column(db.Integer, nullable=False)
    sprite_url =  db.Column(db.String, nullable=False)





