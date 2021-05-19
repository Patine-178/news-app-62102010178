from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, reqparse
from flask_basicauth import BasicAuth
from werkzeug.middleware.proxy_fix import ProxyFix
import food, BMR

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

api = Api(app, version='1.0', title='Food API',
          description='Food API',
          )
basic_auth = BasicAuth(app)

ns_foods = api.namespace('foods', description='FOODS operations')
ns_bmr = api.namespace('foods/BMR/<string:gender>', description='Calculate BMR (male or female)')
ns_edit = api.namespace('foods/<string:food_name>', description='Delete or update')

food_model = api.model('Food',
    {
        'Name': fields.String(required=True, description='Food name', example="EGG"),
        'Kilocalories': fields.Float(required=True, description='Food kilocalories', example=148),
        'Alpha-Carotene': fields.Float(required=True, description='Food alpha carotene', example=0),
        'Beta-Carotene': fields.Float(required=True, description='Food beta carotene', example=0),
        'Carbohydrate': fields.Float(required=True, description='Food carbohydrate', example=1.05),
        'Cholesterol': fields.Float(required=True, description='Food cholesterol', example=432),
        'Choline': fields.Float(required=True, description='Food choline', example=0),
        'Fiber': fields.Float(required=True, description='Food fiber', example=0),
        'Lycopene': fields.Float(required=True, description='Food lycopene', example=0),
        'Manganese': fields.Float(required=True, description='Food manganese', example=0.034),
        'Protein': fields.Float(required=True, description='Food protein', example=11.95),
        'Selenium': fields.Float(required=True, description='Food selenium', example=30.8),
        'Sugar-Total': fields.Float(required=True, description='Food sugar total', example=0),
        'Zinc': fields.Float(required=True, description='Food zinc', example=1.38),
        'Vitamin-B12': fields.Float(required=True, description='Food vitamin B12', example=1.07),
        'Vitamin-B6': fields.Float(required=True, description='Food vitamin B6', example=0.162),
        'Vitamin-C': fields.Float(required=True, description='Food vitamin c', example=0),
        'Vitamin-E': fields.Float(required=True, description='Food vitamin e', example=0),
        'Vitamin-K': fields.Float(required=True, description='Food vitamin k', example=0),
    }
)
bmr_model = api.model('BMR', {
    "BMR": fields.Float(required=True, description='BMR result', example="1730.0")
})

message_model = api.model('Message', {
    "message": fields.String(required=True, description='message alert', example="Food has been edited.")
})

not_found = {
    "Name": None,
        "Kilocalories": None,
        "Alpha-Carotene": None,
        "Beta-Carotene": None,
        "Carbohydrate": None,
        "Cholesterol": None,
        "Choline": None,
        "Fiber": None,
        "Lycopene": None,
        "Manganese": None,
        "Protein": None,
        "Selenium": None,
        "Sugar-Total": None,
        "Zinc": None,
        "Vitamin-B12": None,
        "Vitamin-B6": None,
        "Vitamin-C": None,
        "Vitamin-E": None,
        "Vitamin-K": None
}

@ns_foods.route('/')
class FoodList(Resource):
    @ns_foods.doc('list_foods')
    @ns_foods.marshal_list_with(food_model, code=200)
    def get(self):
        food_name = request.args.get('query')
        cal_less = request.args.get('calLess')
        if food_name != None:
            data = food.read_food_json()
            foods = []
            for item in data:
                if item['Name'].lower() == food_name.lower():
                    foods.append(item)
                    return foods, 200
            return [not_found], 500
        elif cal_less != None:
            data = food.read_food_json()
            foods = []
            for item in data:
                if item['Kilocalories'] < float(cal_less):
                    foods.append(item)
            if len(foods) != 0:
                return foods, 200
            else:
                return [not_found], 500
        else:
            return food.read_food_json(), 200
    
    @basic_auth.required
    @ns_foods.doc('add_food')
    @ns_foods.expect(food_model)
    @ns_foods.marshal_with(food_model, code=200)
    def post(self):
        return food.write_food_json(api.payload), 200

@ns_bmr.route('/')
class BMRCal(Resource):
    @ns_bmr.doc('calculate_bmr')
    @ns_bmr.marshal_with(bmr_model)
    def get(self, gender):
        weight_str = request.args.get('weight')
        height_str = request.args.get('height')
        age_str = request.args.get('age')
        if weight_str != None and height_str != None and age_str != None:
            bmr = BMR.cal_BMR(gender, float(weight_str), float(height_str), int(age_str))
            if bmr != None:
                return {"BMR":bmr}

@ns_edit.route('/')
class FoodEdit(Resource):
    @basic_auth.required
    @ns_edit.doc('delete_food')
    @ns_edit.marshal_with(message_model, code=200)
    def delete(self, food_name):
        status = food.delete_food_json(food_name)
        if status == 200:
            return {"message":"Food has been deleted."}, 200
        elif status == 500:
            return {"message":"Delete fail."}, 500

    @basic_auth.required
    @ns_edit.doc('update_food')
    @ns_edit.marshal_with(message_model, code=200)
    def put(self, food_name):
        food_dict = api.payload
        status = food.update_food_json(food_name, food_dict)
        if status == 200:
            return {"message":"Food has been updated."}, 200
        elif status == 500:
            return {"message":"Update fail."}, 500