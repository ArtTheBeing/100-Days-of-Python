from flask import Flask, render_template
import requests
app = Flask(__name__)
url = 'https://api.npoint.io/481e0423e1501f855ffa'


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
    response = requests.get(url)
    data = response.json()
    return render_template('post.html', num=num, blogs=data)

if __name__ == '__main__':
    app.run(debug=True)

