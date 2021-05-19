from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from security import authenticate, identity
from flask_jwt import JWT,jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-super-secret'
api = Api(app)
jwt = JWT(app, authenticate, identity) # มาจาก security.py 

tasks = [{'id': 1, 'name': 'Do homework'}]

class TodoList(Resource):
    @jwt_required()
    def get(self):
        return jsonify({'tasks': tasks})

    @jwt_required()
    def post(self):
        task = {
            'id': len(tasks) + 1,
            'name': api.payload['name'],
        }
        tasks.append(task)
        return api.payload, 201

api.add_resource(TodoList, '/todo')