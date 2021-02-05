from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Employee

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data/insert' , methods = ['GET','POST'])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
 
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        name = request.form['name']
        age = request.form['age']
        position = request.form['position']
        employee = Employee(employee_id=employee_id, name=name, age=age, position = position)
        db.session.add(employee)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveDataList():
    employees = Employee.query.all()
    return render_template('datalist.html', employees = employees)

@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return "Employee with id ={0} Does not exist".format(id)

@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = Employee(employee_id=id, name=name, age=age, position = position)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return "Employee with id = {0} Does not exist".format(id)
 
    return render_template('update.html', employee = employee)

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    employee = Employee.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect('/data')
        db.abort(404)
 
    return render_template('delete.html')