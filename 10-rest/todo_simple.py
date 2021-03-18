from flask import Flask, request, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = [{'id': 1, 'name': 'Do homework'}]

@api.route('/todo')
class TodoList(Resource):
    def get(self):
        return jsonify({'tasks': tasks})

    def post(self):
        task = {
            'id': len(tasks) + 1,
            'name': api.payload['name'],
        }
        tasks.append(task)
        return api.payload, 201

@api.route('/todo/<int:task_id>')
class Todo(Resource):
    def get(self, task_id):
        task = None
        for t in tasks:
            if t['id'] == task_id:
                task = t

        return jsonify({'task': task})

    def put(self, task_id):
        for i, t in enumerate(tasks):
            if t['id'] == task_id:

                task = {
                    'id': t['id'],
                    'name': api.payload['name'],
                }

                tasks[i] = task

        return api.payload