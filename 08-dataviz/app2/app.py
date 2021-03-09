from flask import Flask, render_template
import json
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Make ข้อมูลขึ้นมาเอง
    rng = pd.date_range('1/1/2020', periods=128, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    # มี 2 graph
    graphs = [
        dict(
            data=[
                dict(
                    x=['A', 'B', 'C', 'D'],
                    y=[30, 20, 40, 15],
                    type='bar'
                ),
            ],
            layout=dict(
                title='bar-graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,
                    y=ts
                )
            ],
            layout=dict(
                title='time-series'
            )
        )
    ]

    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           graphJSON=graphJSON)

@app.route('/scatter-plot')
def scatter_plot():
    n = 500
    random_x = np.random.randn(n) # random x
    random_y = np.random.randn(n) # random y

    # trace ถูกสร้างมาจาก plotly.graph_objs
    trace = [go.Scatter( # ชนิดของ Graph ที่จะ plot
        x=random_x,
        y=random_y,
        mode='markers'
    )]

    graphJSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder) # เรียกใช้ json โยน trace obj แปลงเป็น json string 
    return render_template('scatter.html', plot=graphJSON)

@app.route('/bar-plot')
def bar_plot():
    n = 15
    x = np.linspace(-1, 1, n)
    y = np.random.randn(n)
    df = pd.DataFrame({'x': x, 'y': y})

    trace = [
        go.Bar(
            x=df['x'],
            y=df['y']
        )
    ]

    graphJSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graph.html', description='Bar-graph', plot=graphJSON)

@app.route('/piechart')
def piechart():
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]

    irises_colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)',
                     'rgb(151, 179, 100)', 'rgb(175, 49, 35)']

    trace = [
        go.Pie(
            labels=labels,
            values=values,
            marker_colors=irises_colors
        )
    ]

    graphJSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graph.html', description='Piechart', plot=graphJSON)

@app.route('/appl-income-statement')
def appl_statement():

    STOCK_API_KEY = '8b667c39d02d348c0093bbebced47883'
    ticker = 'AAPL'
    url = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}'
    data = requests.get(url, params={'apikey': STOCK_API_KEY,'period': 'quarter'}).json()
    df = pd.json_normalize(data) # ทำให้เป็น dict

    fig = go.Figure([
        go.Scatter(
            name='revenue',
            x=df['date'],
            y=df['revenue'],
            mode='lines',
            marker=dict(color='red', size=2),
            showlegend=True # ป้ายบอก
            )
        ])

    #fig.update_xaxes(rangeslider_visible=True)


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('graph.html', description='Apple Inc. Income statement', plot=graphJSON)
