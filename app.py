from flask import Flask
from flask import render_template

app = Flask(__name__)

# url_for('static', filename='hello.html')

name = "Aushaif"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route('/hello/<name>')
@app.route('/x')
def hello():
    return render_template('./hello.html', data= name)

app.run(host="0.0.0.0",  port=1001 , debug=False) 