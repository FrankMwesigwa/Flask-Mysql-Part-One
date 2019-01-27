from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret@123!!'

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

