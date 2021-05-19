from flask import Flask, request, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = [{'id': 1, 'name': 'Do homework'}]

@api.route('/todo')
class TodoList(Resource): # class มองว่าเป็น resource ที่ต้อง พำะีพื
    def get(self): # แบบ GET จะ return tasks ทั้งหมด
        return jsonify({'tasks': tasks})

    def post(self): # แบบ POST จะทำการ append task เข้าไปใหม่โดยผ่าน body
        task = {
            'id': len(tasks) + 1,
            'name': api.payload['name'], # api.payload คือ JSON ที่ได้มาจาก request body
        }
        tasks.append(task)
        return api.payload, 201 # กำหนด status code

@api.route('/todo/<int:task_id>')
class Todo(Resource):
    def get(self, task_id):
        task = None
        for t in tasks:
            if t['id'] == task_id:
                task = t

        return jsonify({'task': task})

    def put(self, task_id): # PUT จะใช้ในการ update resource
        for i, t in enumerate(tasks):
            if t['id'] == task_id:

                task = {
                    'id': t['id'],
                    'name': api.payload['name'],
                }

                tasks[i] = task

        return api.payload