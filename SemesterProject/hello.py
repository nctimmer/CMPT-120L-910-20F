from flask import Flask
app = Flask(__name__)

@app.route('/')
#don't think "app" object was actually created
def hello_world():
    return 'Hello, World!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'