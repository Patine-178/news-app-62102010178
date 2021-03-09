from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import quote
from urllib.request import urlopen
import json

app = Flask(__name__)

OPEN_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&APPID={1}"

OPEN_WEATHER_KEY = '59f97de71b0b9c95d51307f7ab7c95b8'

@app.route("/")
def home():
    city = request.args.get('city')
    if not city:
        city = 'bangkok'
    weather = get_weather(city, OPEN_WEATHER_KEY)

    return render_template("home.html", weather=weather)


def get_weather(city,API_KEY):
    query = quote(city) # ทำให้ city เป็น path url ได้ เอาไว้กัน user ใส่ค่ามั่วๆ
    url = OPEN_WEATHER_URL.format(city, API_KEY) # เอาไปแทนที่ในแต่ละตำแหน่งของ OPEN_WEATHER_URL
    data = urlopen(url).read() # return json string
    parsed = json.loads(data) # return json object (dict)
    weather = None
    if parsed.get('weather'):

        description = parsed['weather'][0]['description']
        temperature = parsed['main']['temp']
        city = parsed['name']
        country = parsed['sys']['country']

        weather = {'description': description,
                   'temperature': temperature,
                   'city': city,
                   'country': country
                   }
    return weather