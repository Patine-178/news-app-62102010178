from flask import Flask, render_template, request, jsonify # มี request มาเพิ่ม

app = Flask(__name__)

@app.route('/score', methods=['GET']) # ใช้แบบ GET
def score():
    val1 = request.args.get('val1', default = 1, type = int) # ถ้ามี request ให้ get ตัวที่ชื่อ val1 data type เป็น int
    val2 = request.args.get('val2', default = 0.5, type = float) # default คือ ถ้า get แล้วไม่เจอ
    # ไม่จำเป็นต้องมี default กับ type ก็ได้ 
    return f"val1 is {val1} , val2 is {val2}"

@app.route('/user', methods=['POST']) 
def user():
    data = request.json
    return jsonify(data)
