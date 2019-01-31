from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "Flask@!123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://farmprod:Master@123Q@127.0.0.1/farmprod'

SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


