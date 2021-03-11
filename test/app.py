from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/area/square')
def square():
    width = request.args.get('width', type=float)
    height = request.args.get('height', type=float)
    area = width*height
    return_data = {"width":width, "height":height, "area":area}
    return jsonify(return_data)