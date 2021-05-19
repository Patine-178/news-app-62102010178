import logging
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")


app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.0')

# สร้าง metrics เอง
by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@app.route('/area/circle')
@by_path_counter # เลือกใช้งาน metrics
def circle():
    radius = request.args.get('radius', type = float)
    area = 3.14 * (radius * radius)
    return_data = {"radius":radius, "area":area }
    return jsonify(return_data)


@app.route('/area/rectangle')
@by_path_counter # เลือกใช้งาน metrics
def rectangle():
    width = request.args.get('width', type = float)
    height = request.args.get('height', type = float)
    area = width*height
    return_data = {"widht":width, "height":height, "area":area }
    return jsonify(return_data)

