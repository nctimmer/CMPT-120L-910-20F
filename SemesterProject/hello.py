from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
app.logger.debug('400')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

@app.route('/hello/')
def hello_world():
    return "Hello, ME!"
app.logger.debug('400')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')