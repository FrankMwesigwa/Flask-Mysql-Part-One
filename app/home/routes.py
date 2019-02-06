from flask import abort, render_template
from flask_login import current_user, login_required

from app.home import home

@home.route('/')
def homepage():
    return render_template('index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('admin_dashboard.html', title="Dashboard")