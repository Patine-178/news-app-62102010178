from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class Food(db.Model):
    __tablename__ = "foods"
 
    name = db.Column(db.String(), primary_key=True)
    energy = db.Column(db.Integer())
    protein = db.Column(db.Float())
    fat = db.Column(db.Float())
    carbohydrate = db.Column(db.Float())