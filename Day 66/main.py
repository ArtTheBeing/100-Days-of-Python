from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)

generated_key = 'ajhsfuigiuhasd'

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    
class addform(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('directions_url', validators=[DataRequired()])
    img_url = StringField('image_url', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet?', validators=[DataRequired()])
    has_wifi = BooleanField('Has Wifi?', validators=[DataRequired()])
    has_sockets = BooleanField('Has Sockets?', validators=[DataRequired()])
    can_take_calls = BooleanField('Can Take Calls?', validators=[DataRequired()])
    coffee_price = StringField('Coffe Price', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/random', methods=['GET'])
def get_random_cafe():
    if request.method == 'GET':
        cafes = Cafe.query.all()
        random_cafe = random.choice(cafes)
        return render_template('random.html', cafes=random_cafe.to_dict())
    
@app.route('/all', methods = ['GET'])
def get_all_cafes():
    if request.method == 'GET':
        cafes = db.session.query(Cafe).all()
        for i in range (len(cafes)):
           cafes[i] = cafes[i].to_dict()
        return jsonify(cafes)
    
@app.route('/search', methods=['GET'])
def search_cafe():
    query = request.args.get('loc')
    query = query.title()
    cafes = (db.session.execute(db.select(Cafe).where(Cafe.location == query)))
    all_cafes = cafes.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    
@app.route('/add', methods=['POST', 'GET'])
def add():
    form = addform()
    if form.validate_on_submit():
        cafe = Cafe(
            name = form.name.data,
            map_url = form.map_url.data,
            img_url = form.img_url.data,
            location = form.location.data,
            seats = form.seats.data,
            has_toilet = form.has_toilet.data,
            has_wifi = form.has_wifi.data,
            has_sockets = form.has_sockets.data,
            can_take_calls = form.can_take_calls.data,
            coffee_price = form.coffee_price.data
        )
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    
    return(render_template('add.html', form=form))


@app.route('/update_price/<cafe_id>')
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


@app.route('/closed-cafe/<id>')
def closed(id):
    key = request.args.get('api_key')
    if key == generated_key:
        cafe=db.get_or_404(Cafe, id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit
            return jsonify(response={"success": "Successfully updated the price."})
        else:
            return jsonify(response={'Not found' : 'Not in database'})
        
    else:
        return jsonify(response={'You do not have permission': 'Wrong api-key!'})
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
