from flask import Blueprint, render_template, redirect, request, url_for

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/lookup', methods=['POST'])
def lookup():
    return redirect(url_for('stock.view_stock', ticker=request.form["ticker"]))
