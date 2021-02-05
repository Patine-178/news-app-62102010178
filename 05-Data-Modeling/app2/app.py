from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "secret-key"

db = SQLAlchemy(app)

class Student(db.Model):
   student_id = db.Column('student_id', db.Integer, primary_key = True)
   first_name = db.Column(db.String(80), nullable=False)
   last_name = db.Column(db.String(80), nullable=False)
   age = db.Column(db.Integer())
   phone = db.Column(db.Integer())
   email = db.Column(db.String(120))

@app.route('/')
def home():
   return render_template('home.html', students = Student.query.all() ) # ดึงข้อมูลทั้งหมด

@app.route('/insert_item', methods = ['GET', 'POST'])
def insert():
    if request.method == 'POST':
      if not request.form['firstname'] or not request.form['lastname'] or not request.form['age']:
         flash('Please enter all the fields', 'error')
      else:

        first_name = request.form['firstname']
        last_name = request.form['lastname']
        age = request.form['age']
        phone = request.form['phone']
        email = request.form['email']
          
        student = Student(first_name=first_name, last_name=last_name, age=age, phone=phone, email=email)
         
        db.session.add(student)
        db.session.commit()
        flash('successfully')
        return redirect(url_for('home')) # กำหนดให้ไปที่ home()
    return render_template('insert.html')