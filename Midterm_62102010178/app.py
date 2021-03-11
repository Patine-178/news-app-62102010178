from flask import Flask, render_template,request,redirect
from models import db, Food
import plotly
import plotly.graph_objs as go
import pandas as pd
import json
import requests
import numpy as np

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app) # db = SQLAlchemy(app)

URL = "https://api.calorieninjas.com/v1/nutrition?query={0}"
KEY = "sv/1TzlQR4ZWt3kugOovFg==HhXQzFLVFb97l5Ha"

@app.before_first_request # ก่อนจะ request ครั้งแรก ให้ create_table() ทำงานก่อน
def create_table():
    db.create_all()

@app.route('/')
def index():
    food = Food.query.all()
    protein = []
    all_food = []
    for i in food:
        protein.append(i.protein)
        all_food.append(i.name)
    trace = [go.Bar( # ชนิดของ Graph ที่จะ plot
        x=all_food,
        y=protein,
    )]
    graphJSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', foods=food, graphJSON=graphJSON)

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == 'GET':
        return render_template("search.html")
    if request.method == 'POST':
        food_name = request.form['food']
        url = URL.format(food_name)
        data = requests.get(url, headers={'X-Api-Key':KEY}).json()
        return render_template("search.html", data=data['items'][0]['calories'])

@app.route('/cal', methods=["GET", "POST"])
def cal():
    if request.method == 'GET':
        return render_template("cal.html")

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        BMR = (10*weight) + (6.25*height) - (5*age) + 5
        if not weight or not height or not age:
            return render_template("cal.html", message="** กรุณาใส่ข้อมูลให้ครบถ้วน **")
        return render_template('cal.html', BMR=BMR)
