from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Employee(db.Model):
    __tablename__ = "employee"
 
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"