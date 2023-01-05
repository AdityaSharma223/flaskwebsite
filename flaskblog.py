from flask import Flask, render_template, url_for, flash, redirect
import flask
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ab3f31f23aca274a06007247400222ff'

posts = [
    {
        'author': 'Aditya',
        'title': 'Post 1', 
        'content': 'first post',
        'date_posted': 'April 20, 2018',
        'tags': ['sports', 'football']
    },
    {
        'author': 'Jane',
        'title': 'Post 2', 
        'content': 'second post',
        'date_posted': 'April 21, 2018',
        'tags': ['lifestyle', 'cooking']
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Unsuccessful login. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)

# if __name__ == "__main__":
#     app.run(debug=True)
