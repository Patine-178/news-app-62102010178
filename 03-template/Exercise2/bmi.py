from flask import Flask, render_template, request, redirect
from flask.helpers import url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def bmi_calc():
    bmi = ''
    if request.method == 'POST':
        weight = float(request.form.get('weight')) # ใช้ .form เพราะรับค่ามาจาก form ของ bmi.html
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template("bmi.html",
	                        bmi=bmi)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)
