from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    __tablename__ = "students"

    student_id = db.Column(db.BigInteger(), primary_key=True)
    name = db.Column(db.String(120))
    image = db.Column(db.String(120))