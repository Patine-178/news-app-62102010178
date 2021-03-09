import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import flask

data = pd.read_csv("finance-charts-apple.csv") # อ่านไฟล์ csv
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d") # Format วันที่จากไฟล์ csv
data.sort_values("Date", inplace=True) # เรียงตามวันที่

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

# เพิ่ม html
app.layout = html.Div(
    children=[
        html.H1(children="AAPL",), # เหมือนกับ <h1></h1>
        html.P( # เหมือนกับ <p></p>
            children="Apple inc."
        ),
        dcc.Graph( # วาด Graph
            figure={
                "data": [
                    {
                        "x": data["Date"], # แกน X เป็นวันที่
                        "y": data["AAPL.High"], # แกน Y เป็นราคาสูงสุด
                        "type": "lines", # ประเภทของ Graph
                    },
                ],
                "layout": {"title": "AAPL High"}, # ชื่อ Graph จะอยู่บน Graph
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)