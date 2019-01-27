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











