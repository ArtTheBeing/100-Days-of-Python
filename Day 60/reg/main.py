from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route("/login", methods=["POST"])
def receive_data():
    return f"Name {request.form.get('username')}, Password {request.form['password']}" #KEY HERE IS THAT METHOD DOESNT MATTER. .get and [] do the same thing

if __name__ == "__main__":
    app.run(debug=True)