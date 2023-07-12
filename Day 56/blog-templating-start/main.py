from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blogs = response.json()
    return render_template("index.html", blogs=blogs)

@app.route('/post/<int:num>')
def blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blogs = response.json()
    return render_template('post.html', num=num, blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)
