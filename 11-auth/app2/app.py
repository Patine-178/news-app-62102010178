from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from flask_basicauth import BasicAuth

app = Flask(__name__)
# กำหนด username กับ password
app.config['BASIC_AUTH_USERNAME'] = 'user1'
app.config['BASIC_AUTH_PASSWORD'] = 'abcxyz'
api = Api(app)
basic_auth = BasicAuth(app) # มาจาก class BasicAuth

tasks = [{'id': 1, 'name': 'Do homework'}]

# การเข้าถึง resource
class TodoList(Resource):
    @basic_auth.required # decorator ถ้าจะใช้ function get() จะต้องผ่าน basic_auth ก่อน (ต้อง login ก่อน)
    def get(self):
        return jsonify({'tasks': tasks})

    @basic_auth.required # decorator ถ้าจะใช้ function post() จะต้องผ่าน basic_auth ก่อน (ต้อง login ก่อน)
    def post(self):
        task = {
            'id': len(tasks) + 1,
            'name': api.payload['name'],
        }
        tasks.append(task)
        return api.payload, 201

api.add_resource(TodoList,'/todo') # กำหนด route ให้กับ resource TodoList เหมือนกับ @api.route('/todo')
