from flask import Flask
from flask import render_template, request, flash, redirect
from flask_qrcode import QRcode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'azws1ex123csGGSgGsfdgnmklGFRRDCVBa9s00das'
QRcode(app)


@app.route('/resto')
def resto():
    return render_template('resto.html')


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/menu')
def menu():
    return render_template('menu_page.html')


@app.route('/qr_code', methods=('GET', 'POST'))
def qr_cod(qr=None):
    if request.method == 'POST':
        return render_template('qr_page.html', STRING_TO_ENCODE=request.form['content'])
    return render_template('qr_page.html')
