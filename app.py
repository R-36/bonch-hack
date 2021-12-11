from flask import Flask
from flask import render_template, request, flash, redirect

from flask_qrcode import QRcode
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
app.config['SECRET_KEY'] = 'azws1ex123csGGSgGsfdgnmklGFRRDCVBa9s00das'
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAJi54PgAXM-zIq3maDOy4LZFO0awKmMO4"
QRcode(app)
GoogleMaps(app)


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


@app.route('/map')
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    return render_template('maps_page.html', mymap=mymap, sndmap=sndmap)
