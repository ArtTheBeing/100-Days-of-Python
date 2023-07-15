from flask import Flask, render_template
import requests
app = Flask(__name__)
url = 'https://api.npoint.io/481e0423e1501f855ffa'
response = requests.get(url)
data = response.json()

@app.route('/')
def home_page():
    response = requests.get(url)
    data = response.json()
    return render_template('index.html', blogs=data)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/post/<int:num>')
def post(num):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template('post.html', num=num, blogs=requested_post)

if __name__ == '__main__':
    app.run(debug=True)

