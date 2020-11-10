from flask import Flask
app = Flask(__name__)

@app.route('/')
#don't think "app" object was actually created
def hello_world():
    return 'Hello, World!'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)