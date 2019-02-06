from flask import render_template
from flask_login import login_required

from app.home import home

@home.route('/')
def homepage():
    return render_template('index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title="Dashboard")
