from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, world'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/news')
def news():
    return """<html> 
        <h1>News</h1> 
        <p>SWU News daily topics:</p>
        <ul>
            <li>Technology</li>
            <li>Sport</li>
            <li>Education</li>
        </ul>
    </html>"""

@app.route('/news/tech')
def tech_news():
    return '<b>technology news</b>'

@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)

@app.route('/name/<int:num>')
def favorite_number(num):
    return f"Your favorite number is {num}, which is half of {num * 2}"

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name


app.env="development"
app.run(debug=True)