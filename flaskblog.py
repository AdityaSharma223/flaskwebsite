from flask import Flask, render_template 
app = Flask(__name__)

posts = [
    {
        'author': 'aditya sharma',
        'title': 'WoW such a nice post', 
        'content': 'first post',
        'date_posted': 'April 20th 2018'
    },
    {
        'author': 'Jane',
        'title': 'Post 2', 
        'content': 'second post ',
        'date_posted': 'April 21st 2018'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

# if __name__ == "__main__":
#     app.run(debug=True)
