from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret@123!!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://farmprod:Master@123Q@127.0.0.1/farmprod'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

db.create_all() 

admin = User(username='admin', email='admin@code.com', password='admin@123')
frank = User(username='frank', email='frank@code.com', password='frank@123')
emma = User(username='emma', email='emma@code.com', password='emma@123')

post1 = Post(title='Killer',content='This is how we do it here in londa', user_id=1)
post2 = Post(title='Killer1',content='This is how we', user_id=1)
post3 = Post(title='Killer2',content='This is how we do it here', user_id=1)

db.session.add(admin)
db.session.add(frank)
db.session.add(emma)

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

db.session.commit()

posts = [
    {
        'author': 'Frank Mwesigwa',
        'title': 'Learning Flask',
        'content': 'Flask is awseome and doing so well in programming',
        'date_posted': 'January 27, 2019'
    },
    {
        'author': 'Deus Abigaba',
        'title': 'Emmanuel Ninja',
        'content': 'Video Games conferencing with Ninja man',
        'date_posted': 'January 27, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") 
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST']) 
def register():
    form = RegistrationForm() #create an instance of RegistrationForm Class. we have given our object a name form
    if form.validate_on_submit(): # check if all form fields are valid
        flash(f'Account created for {form.username.data}!', 'success') # show an alert message to the user on screen 
        return redirect(url_for('home')) # Redirect the user back to the home after successful login
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@coding.com' and form.password.data == 'test@123': # hard corded username / password
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug='True')

