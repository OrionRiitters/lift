from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dict = {'crumb': 'crumbs!'}
    return render_template('home.html', dict=dict)
