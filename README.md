
####################################################

Getting Started with Flask Mysql Part One

#####################################################

Flask is a simple, easy-to-use microframework for Python that can help build scalable and secure web applications.
We'll start by installing virtualenv, a tool to create isolated Python environments. 

We need to use virtual environments to keep the dependencies used by different Python projects separate, 
and to keep our global site-packages directory clean.

pip install virtualenv
mkvirtualenv agrosave
cd to your projects folder and create your project folder == mkdir agrosave

### let's install Flask with a few other dependencies that our project will need 
pip install Flask Flask-Restful Flask-SQLAlchemy marshmallow pymysql Flask-Migrate Flask-Script
pip install flask-login Flask-WTF flask-bootstrap

##write the dependencies to the a text 
pip freeze > requirements.txt

################################################

We begin by importing the Flask class, and creating an instance of it. 
We use the __name__ argument to indicate the app's module or package, so that Flask knows where to 
find other files such as templates.
Then we have a simple function that will display the string Hello World!. 
The preceeding decorator simply tells Flask which path to display the result of the function. 
In this case, we have specified the route /, which is the home URL.

####################################################

 A real-world web project usually has many files. 
 It's important to maintain a good directory structure, so as to organize the different components of the application separately. 
 These are a few of the common directories in a Flask project:
 
 /app: This is a directory within my-project . We'll put all our code in here, and leave other files, such as the requirements.txt file, outside.
/app/templates: This is where our HTML files will go.
/app/static: This is where static files such as CSS and JavaScript files as well as images usually go. 

###########################################################

To build our website, we'll need more files that serve various functions. 
Most Flask apps have the following basic file structure:

run.py: This is the application's entry point. We'll run this file to start the Flask server and launch our application.
config.py: This file contains the configuration variables for your app, such as database details.
app/__init__.py: This file intializes a Python module. Without it, Python will not recognize the app directory as a module.
app/views.py: This file contains all the routes for our application. This will tell Flask what to display on which path.
app/models.py: This is where the models are defined. A model is a representation of a database table in code. 

├── my-project
       ├── app
       │   ├── __init__.py
       │   ├── templates
       │   └── views.py
       ├── config.py
       ├── requirements.txt
       └── run.py

#####################################################

#config.py 
# Enable Flask's debugging features. Should be False in production
DEBUG = True

#####################################################

Next, we have to initialize our app with all our configurations. 
This is done in the app/__init__.py file. Note that if we set instance_relative_config to True, 
we can use app.config.from_object('config') to load the config.py file

# app/__init__.py
from flask import Flask
# Initialize the app
app = Flask(__name__, instance_relative_config=True)
# Load the views
from app import views
# Load the config file
app.config.from_object('config')

#####################################################

# All we have to do now is configure our run.py file so we can start the Flask server.
# run.py

from app import app

if __name__ == '__main__':
    app.run()


# To use the command flask run like we did before, we would need to set the FLASK_APP environment variable to run.py, like so:
set FLASK_APP=run.py
flask run

#####################################################

 We use the @app.route decorator to specify the path we'd like the view to be dispayed on.
#views.py
from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")
	   

Flask provides a method, render_template, which we can use to specifiy which HTML file should be loaded in a particular view

# Templates
cd app/templates
touch base.html index.html about.html

#### base.html ######################################################
<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{% block title %}{% endblock %}</title>
    <!-- Bootstrap core CSS -->
    <link href="static/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->

  </head>
  <body>
    <div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation"><a href="/">Home</a></li>
            <li role="presentation"><a href="/about">About</a></li>
            <li role="presentation"><a href="#" target="_blank">More About Flask</a></li>
          </ul>
        </nav>
      </div>
      {% block body %}
      {% endblock %}
      <footer class="footer">
        <p>© 2019 Coding Bootcamp Academy</p>
      </footer>
    </div> <!-- /container -->
  </body>
</html>

##########################################################################

<!-- index.html-->

{% extends "base.html" %}
{% block title %}Home Page{% endblock %}
{% block body %}
<div class="jumbotron">
  <h1>Flask Is Awesome</h1>
  <p class="lead">And I'm glad to be learning so much about it!</p>
</div>
{% endblock %}

#########################################################################

<!-- about.html-->

{% extends "base.html" %}
{% block title %}About us{% endblock %}
{% block body %}
<div class="jumbotron">
  <h1>The About Page</h1>
  <p class="lead">You can learn more about my website here.</p>
</div>
{% endblock %}
	   
###########################################################################

We use the {% extends %} tag to inherit from the base template. We insert the dynamic content inside the {% block %} tags. 
Everything else is loaded right from the base template, so we don't have to re-write things that are common to all pages, 
such as the navigation bar and the footer.
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   