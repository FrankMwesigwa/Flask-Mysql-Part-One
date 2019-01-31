from flask import render_template, url_for, flash, redirect, request
from src.models import Post

common = Blueprint('common', __name__)

@common.route("/")
@common.route("/home")
def home():
    return render_template('home.html', posts=posts)


@common.route("/about") 
def about():
    return render_template('about.html', title='About')