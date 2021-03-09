from flask import Flask, render_template

from stocks.blueprints.home import home
from stocks.blueprints.stock import stock
from stocks.config import configurations

def create_app(environment_name='dev'):
    app = Flask(__name__)

    app.config.from_object(configurations[environment_name])

    app.register_blueprint(home)
    app.register_blueprint(stock)

    return app
