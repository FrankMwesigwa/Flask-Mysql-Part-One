In this series of lessons we will be learning how to build a Fully Featured web application using the Flask framework and python. Flask is a microframework that makes it very enjoyable to work with these backend applications.

Part One : Setting up a Flask application

we start off by installing the packages that we shall be using in our application. its always a good idea to seperate different projects in their own virtual environments

We'll start by installing virtualenv, a tool to create isolated Python environments. We need to use virtual environments to keep the dependencies used by different Python projects separate and to keep our global site-packages directory clean.

pip install virtualenv
mkvirtualenv flaskapp
workon flaskapp
deactivate
cd to your projects folder and create your project directory = mkdir flaskapp

Let's now install the Flask Package by running the command below
These commands should now be run in your project directory i.e flaskapp
pip install Flask

we can start that our Flask installation was succesfully by going to cmd and typing:
type python on command prompt to get the python interpretaor 
>>> import flask

we now have a completely empty project directory. within the directory lets create a new file called run.py

####### run.py ######
from flask import Flask -- here we are importing the Flask class from the flask package 

app = Flask(__name__) -- here we are creating the app variable and setting it to an instance of the Flask class                            and passing in a special variable name in python which is just the name of the module

@app.route("/") -- here we are creating our routes. routes are what we type in our browser to go to different pages
def hello():
    return "<h1>Home Page !!</h1>"

@app.route("/about") 
def about():
    return "<h1>About us Page !!</h1>"

if __name__ == '__main__':
    app.run(debug='True')
#######

To start the development server execute command below on command prompt:
python run.py

Part Two: Using Templates

create a new folder called templates. inside the templates folder create home.html and about.html files
we use the render_template method in flask package to use html templates in flask

#lets use some dummy data here since we dont have a databse yet
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

we can pass the posts call within our render_template
@app.route("/")
def hello():
    return render_template('home.html' , posts=posts)

Flask uses a templating engine called Jinja2 and it allows us to write code within our template. This is how a code block is written in jinja2
  {% %}
  {% %}

a variable in jinja2 has got 2 cury braces
  {{}}

  {% for post in posts %}
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author }} on {{ post.date_posted }}</p>
    <p>{{ post.content }}</p>
  {% endfor %}

we can also use if else statements in jinja2 templates
  {% if title %}
    <title> Flask App - {{ title }} </title>
  {% else %}
    <title> Flask App </title>
  {% endif %}

Template Inheritance
Its always better to have every thing that is repeated in a single place so that there is only one place to make changes . we can achieve this using template heritance 

create a new html file called layout.html and pick out all the repeated stuff from other html files. The only thing that is different is the body section from all files.

  {% block content %}
  {% endblock %}

  {% extends "layout.html" %}
    {% block content %}
        {% for post in posts %}
            <h1>{{ post.title }}</h1>
            <p>By {{ post.author }} on {{ post.date_posted }}</p>
            <p>{{ post.content }}</p>
        {% endfor %}
    {% endblock content %}

Bootstrap is a nice library that makes it very easy to add nice styles to our website 
you might also want to use the flask-bootstarp library if you are interested in it

url_for
for links we shall be using the url_for provided by the flask library 

Creating Forms and Validation
we shall use a flask extension for working with forms in flask. its called flask-wtf
pip install flask-wtf

lets create a file where we can put these files called forms.py 
we create class forms in flask and these inherit from the FlaskForm

from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):

when working with forms we need to set a secret key for our application. This will help us in avoiding cross-siting validations

In our routes we need to create instance of our forms e.g
 form = RegistrationForm()

In the render_template we pass in the form object so that our objects can have that instance 
    @app.route("/login") 
    def login():
        form = LoginForm()
        return render_template('login.html', title='Login', form=form)

Lets now create our 2 template files register.html and login.html

we use flash to send alerts to the screens. first import it from flash
    flash(f'Account created for {form.username.data}!', 'success')

### Database with Flask-SQLAlchemy
In python we shall be using SQLAlchemy which is a popular ORM . ORM stands for object relation mapper. it allows us to access our database in an object oriented way and you can use diffirent databases without changing your python code.

First we need to install the flask-sqlalchemy
pip install flask-sqlalchemy

Now import the sqlalchemy package into our application in the run.py file 
After importing package we need to specify the URL of where the database is located
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://farmprod:Master123@127.0.0.1/farmprod'

After creating the database path we now need to create a database instance and pass in app as an argument
    db = SQLAlchemy(app)

In sqlalchemy we can represent our database structure as class models. Each class is going to be its own table in the database

we create the class and import from db.Model
    class User(db.Model)

This is a redadant method or a special method which is a represenation of how our class will look like when printed out.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

The backref adds other column to our model

Open Command Prompt
type python
>>> from agrosave import db
db.create_all() -- this will create our database in mysql
admin = User(username='admin', email='admin@code.com', password='admin@123')
frank = User(username='frank', email='frank@code.com', password='frank@123')
emma = User(username='emma', email='emma@code.com', password='emma@123')

db.session_add(admin)
db.session_add(frank)
db.session_add(emma)

db.session_commit() // here we are saving the data in the database

To get all users in the database we run command below
    user.query.all()

To get the first user from the list run command below
    user.query.first()

To fliter we use the command below
    user.query.filter_by(username='frank').all()
    user.query.filter_by(username='frank').first()
    user = user.query.filter_by(username='frank').first()

To get a user with a specific id
    user = user.query.get(1)

To get the user's post
    user.post

Lets add posts to our database
    post1 = Post(title='Killer',content='This is how we do it here in londan', user_id='user.id')
    post2 = Post(title='Killer',content='This is how we do it here in londan', user_id='user.id')
    post3 = Post(title='Killer',content='This is how we do it here in londan', user_id='user.id')

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)

    db.session.commit()

    user.posts

    for post in user.posts:
        print(post.title)
    
    post = Post.query.first() -- this will query and return the first post
    post.user_id
    post.author

    db.drop.all()
























