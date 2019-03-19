from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    dict = {'crumb': 'Yes'}
    return render_template('home.html', dict=dict)

@app.route('/templates/<template>', methods=['GET'])
def start_workout(template):
    return render_template(template)

#@app.route('/public/css/<file>', methods=['GET'])
#def serve_css(file):
#    return send_from_directory('public/css', file)
#
#@app.route('/node_modules/bootstrap/dist/css/<file>', methods=['GET'])
#def serve_bootstrap(file):
#    return send_from_directory('node_modules/bootstrap/dist/css', file)
