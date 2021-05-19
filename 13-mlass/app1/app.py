import os
from flask import Flask, request, render_template, jsonify
from PIL import Image
import base64
from ml_model import TFModel

UPLOAD_FOLDER = './static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # path ที่จะทำการ upload ภาพที่ user ใส่เข้ามา

model = TFModel(model_dir='./ml-model/') # directory ของ saved_model.pb
model.load() # ทำการ load model เพื่อเตรียมใช้งาน

@app.route('/dogcat', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files: # request.files = {'file1':...}
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        # ทำการ save image file ไว้ใน static/uploads
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename) # (กำหนด path, ชื่อ file)
        file1.save(path)

        image_1 = Image.open(path) # ใช้ pillow ในการเปิด image
        outputs = model.predict(image_1)

        return render_template('prediction.html', pred_result=outputs)

    return render_template('upload.html')

