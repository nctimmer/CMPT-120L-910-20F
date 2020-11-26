from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
app.logger.debug('400')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/personality/')
def personality():
    return render_template("personality.html")

if __name__ == '__main__':
    app.run(debug=True)
