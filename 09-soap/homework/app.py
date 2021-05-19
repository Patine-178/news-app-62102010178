from flask import Flask,render_template, request
from zeep import Client

wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl=wsdl)

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'] )
def country_flag():
    country_image = None
    if request.method == 'POST':
        country_code = request.form['country']
        country_image = client.service.CountryFlag(country_code)
    return render_template('searchFlag.html', country_image=country_image)