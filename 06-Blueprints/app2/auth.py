from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('main.profile'))
    else:
       return render_template('login.html')

@auth.route('/logout')
@login_required # มาจาก flask login จะทำงานก็ต่อเมื่อ login แล้ว
def logout():
    logout_user()
    return redirect(url_for('main.index'))
