from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__) # สร้าง Blueprint

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)
