from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
 
    title = db.Column(db.String(), primary_key=True)
    author = db.Column(db.String())
    genre = db.Column(db.String())
    height = db.Column(db.Integer())
    publisher = db.Column(db.String())