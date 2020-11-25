from flask import Flask, render_template
app = Flask(__name__)

# So this is how multiple paths could be set up.

@app.route('/')
def index():
    app.logger.info("User headed to the Index Page")
    return render_template('index.html')

@app.route('/home')
def home():
    app.logger.info("User headed to the Home Page")
    return render_template('home.html')

@app.route('/about')
def about():
    app.logger.info("User headed to the About Page")
    return render_template('about.html')

@app.route('/personality')
def personality():
    app.logger.info("User headed to the Personality Page")
    return render_template('personality.html')

@app.route('/404')
def fourzerofour():
    app.logger.info("User headed to the 404 Page. This is a test tho so it's info rather than warning.")
    return render_template('page_not_found.html')

# This one is important. This is our you're lost. Anytime they go to a route that you don't have defined they get sent here. 
@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning("User headed to the 404 Page")
    return render_template('page_not_found.html'), 404