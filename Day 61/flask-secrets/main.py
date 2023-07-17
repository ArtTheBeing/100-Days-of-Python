from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

#Form Creation with fields
class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Length(min=4, message='Longa'), Email(message='That aint no email foo')])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=4, message='Longa')])
    submit = SubmitField(label="log in")

app = Flask(__name__)
app.secret_key = "ashfieafbnajf"

bootstrap = Bootstrap5(app)

target_email = 'admin@email.com'
target_password = '12345678'

@app.route("/")
def home():
    return render_template('index.html')

#Need to include recievable methods
@app.route('/login', methods=['POST', 'GET'])
def login():
    #Create form
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == target_email and form.password.data == target_password:
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
