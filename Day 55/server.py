import random
from flask import Flask
app = Flask(__name__)


global number 
number = random.randint(1,9)


@app.route('/')
def home():
    return 'Welcome to higher or lower. Add a "/" and a number between 1-9 to guess a number'

@app.route('/<int:url>')
def check(url):
    if url == number:
        return('Correct')
    elif url < number:
        return('Higher')
    elif url > number:
        return('Lower')

if __name__ == '__main__':
    app.run(debug=True) #Run in debug mode

# def check_number(url):
#     def wrapper():
#         if url == number:
#             return('Correct')
#         elif url < number:
#             return('Higher')
#         elif url > number:
#             return('Lower')
#     return wrapper