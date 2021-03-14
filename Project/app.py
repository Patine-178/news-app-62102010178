from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, Students
from blueprints.home import home
from blueprints.dev import dev_name
from blueprints.search import search

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(home)
app.register_blueprint(dev_name)
app.register_blueprint(search)

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()