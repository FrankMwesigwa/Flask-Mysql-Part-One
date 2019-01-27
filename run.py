from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about") 
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug='True')

