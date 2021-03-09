from flask import Blueprint, render_template, current_app
import requests

stock = Blueprint('stock', __name__, url_prefix='/stocks')

@stock.route('/<string:ticker>/quote')
def view_stock(ticker):

    url = '{}/stock/real-time-price/{}'.format(current_app.config['STOCK_API_BASE_URL'], ticker)
    data = requests.get(url, params={'apikey': current_app.config['STOCK_API_KEY']}).json()
    stock_price = data["price"]
    return render_template('stock/stock_quote.html', ticker=ticker, stock_price=stock_price)

@stock.route('/<string:ticker>/financials')
def financials(ticker):
    url = '{}/financials/income-statement/{}'.format(current_app.config['STOCK_API_BASE_URL'], ticker)
    data = requests.get(url, params={'apikey': current_app.config['STOCK_API_KEY'],'period': 'quarter'}).json()
    financials = data["financials"]
    financials.sort(key=lambda quarter: quarter["date"])

    chart_data = [float(q["EPS"]) for q in financials]
    chart_params = {"type": 'line',
                    "data": {
                        'labels': [q["date"] for q in financials],
                        'datasets': [{'label': 'EPS', 'data': chart_data}]
                    }}

    return render_template('stock/financials.html', ticker=ticker, financials=financials, chart_params=chart_params)


