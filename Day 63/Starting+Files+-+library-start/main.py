from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-coolection.db"
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.rating)).scalars()
    return render_template('index.html', books=all_books)

@app.route("/add", methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        #all_books.append({'title': request.form['title'], 'author': request.form['author'], 'rating': request.form['rating']})
        book = Books(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/update", methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        update_book = db.get_or_404(Books, id)
        update_book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    id = request.args.get('id')
    update_book = db.get_or_404(Books, id)
    return render_template('update.html', book=update_book)

@app.route("/delete", methods=['POST', 'GET'])
def delete():
    id = request.args.get('id')
    delete_book = db.get_or_404(Books, id)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

