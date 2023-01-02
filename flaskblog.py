from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Aditya',
        'title': 'Post1 ', 
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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

# if __name__ == "__main__":
#     app.run(debug=True)
