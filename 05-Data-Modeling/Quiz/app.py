from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Books

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    books = Books.query.all()
    return render_template('home.html', books = books)

@app.route('/insert', methods=["GET", "POST"])
def insert():
    if request.method == 'GET':
        return render_template("insert.html")

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        height = request.form['height']
        publisher = request.form['publisher']
        if not title or not author or not genre or not height or not publisher:
            return render_template("insert.html", message="** กรุณาใส่ข้อมูลให้ครบถ้วน **")
        book = Books(title=title, author=author, genre=genre, height=height, publisher=publisher)
        db.session.add(book)
        db.session.commit()
        return redirect('/')

@app.route('/update/<string:title>', methods=["GET", "POST"])
def update(title):
    book = Books.query.filter_by(title=title).first()
    if request.method == 'POST':
        if book:
            book.title = request.form['title']
            book.author = request.form['author']
            book.genre = request.form['genre']
            book.height = request.form['height']
            book.publisher = request.form['publisher']
            db.session.commit()
            return redirect('/')

    return render_template("update.html", book=book)

@app.route('/delete/<string:title>', methods=["GET", "POST"])
def delete(title):
    book = Books.query.filter_by(title=title).first()
    if request.method == 'GET':
        if book:
            db.session.delete(book)
            db.session.commit()
            return redirect('/')