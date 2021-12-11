from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/resto')
def resto():
    return render_template('resto.html')


@app.route('/')
def hello():
    return render_template('main.html')
