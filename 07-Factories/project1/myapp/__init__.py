from flask import Flask, render_template
from myapp.blueprints.main import main
from myapp.blueprints.auth import auth
from myapp.config import configurations


def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
