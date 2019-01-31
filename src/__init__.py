from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

app = Flask(__name__)
app.config_from_object(Config)

db = SQLAlchemy(app)

from src.users.routes import users
from src.posts.routes import posts
from src.common.routes import common

app.register_blueprint(users)
app.register_blueprint(routes)
app.register_blueprint(common)
