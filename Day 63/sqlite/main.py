import sqlite3

# db = sqlite3.connect("sqlite/books-collection.db")
# cursor = db.cursor()
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-coolection.db" #This creates Database
db.init_app(app)

class Books(db.Model): #This creates table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context(): #This creates all specified tables that have not been created yet
    #db.create_all()
    book = Books(id=1, title='Harry Potter', author='J.K Rowling', rating=8.1)
    db.session.add(book)
    db.session.commit()

with app.app_context():
    #For specific book
    #book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    
    #for all books
    result = db.session.execute(db.select(Books).order_by(Books.rating))
    all_books = result.scalars()

    #To Update by query
    #update_book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    # update_book.title = "Something"
    # db.session.commit()

    #To Update by ID
    # book_id = 1
    # update_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or update_book = db.get_or_404(Books, book_id)
    # update_book.title = "Something"
    # db.session.commit()

    #To delete by ID
    # book_id = 1
    #delete_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or delete_book = db.get_or_404(Books, book_id)

    #The .get_or_404 only works with primary key aka id