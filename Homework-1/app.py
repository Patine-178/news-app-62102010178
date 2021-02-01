from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import quote, uses_query
from urllib.request import urlopen
import json

app = Flask(__name__)

COVID_URL = "http://newsapi.org/v2/top-headlines?country=th&q=%E0%B9%82%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%94&apiKey=1214a275280a44e3beffa61ef9510fed"
NEWS_URL = "http://newsapi.org/v2/top-headlines?country={0}&q={1}&apiKey=1214a275280a44e3beffa61ef9510fed"

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&lang=th&appid=309fe7ce47b61de19535bda5bdf081fd"
IMG_URL = "http://openweathermap.org/img/wn/{0}@2x.png"

@app.route('/')
def home():
    # 5 ข่าว Covid-19
    data = urlopen(COVID_URL).read()
    parsed = json.loads(data)
    covid_new = []
    for i in range(0, 5):
        covid_new.append({"head":parsed['articles'][i]['title'], 
            "content":parsed['articles'][i]['description'], 
            "img":parsed['articles'][i]['urlToImage'], 
            "url":parsed['articles'][i]['url']})

    # สภาพอากาศ ณ เวลานี้ของแต่ละเมือง
    city = request.args.get('city')
    if not city:
        city = "Bangkok"
    weather = get_weather(city)
    return render_template("home.html", news=covid_new, weather=weather)

def get_weather(city):
    query_city = convert_to_unicode(city)
    url = WEATHER_URL.format(query_city)
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get('weather'):
        temperature = parsed['main']['temp']
        description = parsed['weather'][0]['description']
        pressure = parsed['main']['pressure']
        humidity = parsed['main']['humidity']
        wind = parsed['wind']['speed']
        max_min = str(parsed['main']['temp_max']) + "/" + str(parsed['main']['temp_min'])
        city = parsed['name']
        country = parsed['sys']['country']
        img = IMG_URL.format(parsed['weather'][0]['icon'])

        weather = {'temperature': temperature, 
                   'description': description,
                   'pressure': pressure,
                   'humidity':humidity,
                   'wind':wind,
                   'max_min':max_min,
                   'city': city,
                   'country': country,
                   'img':img
                   }
    return weather

@app.route("/search")
def search():
    country = request.args.get('country')
    keyword = request.args.get('keyword')
    if not country and not keyword:
        return render_template("search.html", news=[0,])
    elif not country:
        country = 'th'
    elif not keyword:
        keyword = 'covid-19'
    news = get_news(country, keyword)
    return render_template("search.html", news=news)

def get_news(country, keyword):
    query_country = quote(country)
    query_keyword = convert_to_unicode(keyword)
    url = NEWS_URL.format(query_country, query_keyword)
    data = urlopen(url).read()
    parsed = json.loads(data)
    news = [len(parsed['articles'])]
    for i in range(len(parsed['articles'])):
        head = parsed['articles'][i]['title']
        content = parsed['articles'][i]['description']
        link = parsed['articles'][i]['url']
        news.append({"head":head, "content":content, "url":link})
    return news

@app.route("/about")
def about():
    return render_template("about.html")

def convert_to_unicode(txt):
    convert = str(txt.encode())[2:].replace("\\x", "%")
    encode = convert[:len(convert)-1]
    return encode
