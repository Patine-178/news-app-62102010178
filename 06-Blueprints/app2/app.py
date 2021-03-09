from flask import Flask
from main import main
from auth import auth
from flask_sqlalchemy import SQLAlchemy
from models import db,User
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'app-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


app.register_blueprint(main)
app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
