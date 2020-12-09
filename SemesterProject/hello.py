from flask import Flask
from flask import render_template
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

#home page
@app.route('/')
def index():
    return render_template("index.html")

#about page
@app.route('/about/')
def about():
    return render_template("about.html")

#contact page
@app.route('/contact/')
def contact():
    return render_template("contact.html")

#personality page
@app.route('/personality/')
def personality():
    return render_template("personality.html")

#404 error non-existent page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
