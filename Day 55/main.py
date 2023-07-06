from flask import Flask
app = Flask(__name__)
#print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'

@app.route('/bye')
def say_bye():
    return 'Bye'

@app.route('/username/<name>/<int:number>/') #Saves the path as the name
def greet(name, number):
    return f'Hello {name}! you are {number} years old'

if __name__ == '__main__':
    app.run(debug=True) #Run in debug mode