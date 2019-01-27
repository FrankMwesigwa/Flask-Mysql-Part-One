In this series of lessons we will be learning how to build a Fully Featured web application using the Flask framework and python. Flask is a microframework that makes it very enjoyable to work with these backend applications.

Lets get started learning how to use Flask

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




