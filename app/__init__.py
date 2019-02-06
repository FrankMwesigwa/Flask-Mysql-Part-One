from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = "Flask@!123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://farmprod:Master@123Q@127.0.0.1/farmprod'

SQLALCHEMY_TRACK_MODIFICATIONS = False

Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager()

login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

from app import models

from app.home import home
from app.auth import auth

app.register_blueprint(home)
app.register_blueprint(auth)
