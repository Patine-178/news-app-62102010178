from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # บอก database ที่จะใช้ (SQLite และ ชื่อ database)
db = SQLAlchemy(app) # ตัวจัดการ database ทั้งหมด

# User table
class User(db.Model): # สืบทอด db.Model (ถ้าต้องให้ class เป็นตาราง ต้องสืบทอด db.Model)
    id = db.Column(db.Integer, primary_key=True) # สร้าง column ชือ id เป็น ini และ เป็น primary key
    username = db.Column(db.String(80), unique=True, nullable=False) # เป็น string ห้ามเป็น null
    email = db.Column(db.String(120), unique=True, nullable=False) # เป็น string ห้ามเป็น null





