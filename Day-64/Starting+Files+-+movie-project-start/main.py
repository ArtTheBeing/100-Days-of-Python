from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests
import os

TMDBApi = os.environ.get('TMDB')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db = SQLAlchemy()
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False,)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String, nullable=False)

class AddForm(FlaskForm):
    title  = StringField('title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditForm(FlaskForm):
    rating = FloatField('rating')
    review = StringField('review')
    submit = SubmitField('Submit')

# with app.app_context():
#     db.create_all()
#     new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    all = movies.all()

    for i in range(len(all)):
        all[i].ranking = len(all)-i
    db.session.commit()

    return render_template("index.html", movies=all)

@app.route("/add", methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        apiurl = 'https://api.themoviedb.org/3/search/movie'
        response = requests.get(apiurl, params={'query': form.title.data, 'api_key': TMDBApi}).json()['results']
        return render_template('select.html', list=response)
    
    return render_template('add.html', form=form)

@app.route("/edit", methods=['POST', 'GET'])
def edit():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie=movie)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/new-movie', methods=['POST', 'GET'])
def selection():
    id = request.args.get('id')
    if id:
        url = f"https://api.themoviedb.org/3/movie/{id}"
        response = requests.get(url, params={'api_key' : TMDBApi, 'language' : 'en-US'}).json()
        new_movie = Movie(
            title=response["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=response["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/original{response['poster_path']}",
            description=response["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        movie = db.session.execute(db.select(Movie).where(Movie.title == response['title'])).scalar()
        return redirect(url_for('edit', id=movie.id))

if __name__ == '__main__':
    app.run(debug=True)
