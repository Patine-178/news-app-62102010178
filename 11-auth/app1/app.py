from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [{'id': 1, 'name': 'Do homework'}]
APPKEY = 'HAiOjE2MTY3NjM1OTI'

@app.route('/todo')
def index():
    #auth = request.headers.get("X-Api-Key")
    auth = request.args.get("apikey") # Get request จาก URL
    if auth == APPKEY:
        return jsonify({'tasks': tasks})
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
