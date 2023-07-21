from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# team = db.Table("team",
#    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
#    db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id")))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    team = db.relationship("Pokemon", secondary="team")

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def catch(self, pokemon):
        t = Team(self.id, pokemon.id)
        db.session.add(t)
        db.session.commit()

    def release_poke(self, pokemon):
        t = Team.query.filter_by(user_id=self.id).filter_by(pokemon_id=pokemon.id).first()
        db.session.delete(t)
        db.session.commit()

    def get_team(self):
        t = Team.query.filter_by(user_id=self.id).all()
        team = [Pokemon.query.get(obj.pokemon_id) for obj in t]
        return team
    
    def get_team_length(self):
        t = Team.query.filter_by(user_id=self.id).all()
        team = [Pokemon.query.get(obj.pokemon_id) for obj in t]
        return len(team)
    
    def start_battle(self, opponent_team, user_team):

        opponent_stats = {"HP":0, "Attack":0, "Defense":0}
        for pokemon in opponent_team:
            opponent_stats["HP"] += pokemon.base_hp
            opponent_stats["Attack"] += pokemon.base_att
            opponent_stats["Defense"] += pokemon.base_def
        print(opponent_stats)

        user_stats = {"HP":0, "Attack":0, "Defense":0}
        for pokemon in user_team:
            user_stats["HP"] += pokemon.base_hp
            user_stats["Attack"] += pokemon.base_att
            user_stats["Defense"] += pokemon.base_def
        print(user_stats)
        # returns true if opponent takes more damage than user, false otherwise
        return ((opponent_stats["HP"] - (user_stats["Attack"] - opponent_stats["Defense"])) < (user_stats["HP"] - (opponent_stats["Attack"] - user_stats["Defense"])))




class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name =  db.Column(db.String(100),nullable=False)
    ability =  db.Column(db.String(100),nullable=False)
    base_hp =  db.Column(db.Integer, nullable=False)
    base_att =  db.Column(db.Integer, nullable=False)
    base_def =  db.Column(db.Integer, nullable=False)
    sprite_url =  db.Column(db.String, nullable=False)
    # team = db.relationship("team", secondary=team, lazy="dynamic")

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))

    def __init__(self, user_id, pokemon_id):
        self.user_id = user_id
        self.pokemon_id = pokemon_id












