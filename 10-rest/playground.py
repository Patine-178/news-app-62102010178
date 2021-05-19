from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app) # สร้าง API object โดยกำหมดให้ app

# เป็น api route
@api.route('/hello')
class HelloWorld(Resource): # สร้าง class
    def get(self): # ในรูปแบบ GET
        return {'hello': 'world'}


