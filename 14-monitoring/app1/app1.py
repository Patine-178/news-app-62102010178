from flask import Flask, request, jsonify
import flask_monitoringdashboard as dashboard # เปิด dashboard ได้

app = Flask(__name__)
dashboard.config.init_from(file='./dashboard.cfg')
dashboard.bind(app) # bind(เชื่อมต่อ) กับตัว flask app

@app.route('/area/circle')
def circle():
    radius = request.args.get('radius', type = float)
    area = 3.14 * (radius * radius)
    return_data = {"radius":radius, "area":area }
    return jsonify(return_data)

@app.route('/area/rectangle')
def rectangle():
    width = request.args.get('width', type = float)
    height = request.args.get('height', type = float)
    area = width*height
    return_data = {"widht":width, "height":height, "area":area }
    return jsonify(return_data)