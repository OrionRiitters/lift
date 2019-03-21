from flask import Flask, render_template, send_from_directory, url_for
from python.db_handler import DBHandler

app = Flask(__name__)
db_handler = DBHandler()

@app.route('/', methods=['GET'])
def home():
    """
    Take me home!
    """
    return render_template('home.html')

@app.route('/templates/<template>', methods=['GET'])
def start_workout(template):
    """
    Renders template found in URL of the request.
    """
    db_handler.selector(template)
    return render_template(template, dict=dict)
