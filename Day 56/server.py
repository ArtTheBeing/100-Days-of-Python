from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.date.today().year
    random_num = random.randint(1, 10)
    return render_template('index.html', num=random_num, copy=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f'https://api.agify.io?name={name}')
    age = response.json()['age']
    response = requests.get(f'https://api.genderize.io?name={name}')
    gender = response.json()['gender']
    return render_template('agify.html', name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)