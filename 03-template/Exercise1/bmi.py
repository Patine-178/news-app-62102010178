from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['GET'])
def bmi():
    weight = request.args.get('weight', type = float)
    height = request.args.get('height', type = float)
    h_m = height / 100
    bmi = weight / (h_m**2)
    return f"bmi is {bmi:.2f}"

@app.route('/bmi2', methods=['POST']) 
def bmi2():
    data = request.json # "{"weight":66.0, "height":175.00}"
    weight = data['weight']
    height = data['height']

    h_m = height / 100
    bmi = round(weight / (h_m**2),2)

    return_data = {"weight":weight, "height":height, "bmi":bmi}

    return jsonify(return_data)