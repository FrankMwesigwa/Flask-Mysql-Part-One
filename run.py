from flask import Flask # here we are importing the Flask class from the flask package 

app = Flask(__name__) # here we are creating the app variable and setting it to an instance of the Flask class                            and passing in a special variable name in python which is just the name of the module

@app.route("/") # here we are creating our routes. routes are what we type in our browser to go to different pages
def hello():
    return "<h1>Home Page !!</h1>"

@app.route("/about") 
def about():
    return "<h1>About us Page !!</h1>"

if __name__ == '__main__':
    app.run(debug='True')
