from flask import Flask, render_template, request
import requests
from smtplib import SMTP
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


def email()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/form-entry', methods=["POST"])
def recieve_data():
    if request.method == "POST":
        data = request.form
        ''' UNCOMMENT THIS IN ORDER FOR THE BLOG TO SEND WEBSTIE. TEMPLATE LIKE THIS FOR GIT PURPOSES
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #This line secures the connection and encrypts the email incase anyone sees it along its way
            connection.login(user=my_email, password= pword)
            connection.sendmail(from_addr =my_email, 
                                to_addrs= "to_email", 
                                msg= f"data[name], data[email], data[message]")
                                  '''
        return "<h1>Succesfully sent your message </h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)


