from flask import Flask
from config import Config
from flask_migrate import Migrate
from app.models import db, User
#from . api import api
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
#app.register_blueprint(api)

db.init_app(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from . import routes, models

    