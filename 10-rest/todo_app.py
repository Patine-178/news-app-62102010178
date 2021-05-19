from flask import Flask, jsonify, request

app = Flask(__name__)

# เก็บ task เป็น list ไว้ดูสิ่งที่ต้องทำ
tasks = [{'id': 1, 'task': 'Do homework'}, {'id': 2, 'task': 'Play Valorant'}]

# route แสดง task ทั้งหมดในรูปแบบ JSON
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'todos': tasks})

# route แสดง task ตาม id ที่กำหมดผ่าน URL ในรูปแบบ JSON
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):

    task = None
    for t in tasks:
        if t['id'] == task_id:
            task = t
    return jsonify({'task': task})

# สร้างและแสดง task โดยส่งผ่าน body
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    task = {
        'id': len(tasks) + 1,
        'task': request.json['task'], # ได้รับค่าจาก body
    }
    tasks.append(task)
    return jsonify({'task': task}), 201