from flask import Flask
app = Flask(__name__)

@app.route('/')
#don't think "app" object was actually created
def hello_world():
    return 'Hello, World!'