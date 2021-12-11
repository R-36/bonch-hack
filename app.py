from flask import Flask
from flask import render_template, request, flash, redirect

from flask_qrcode import QRcode
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import datetime

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


@app.route('/resto/scheme')
def scheme2():
    table_cords = {
        'table1': "10,49,68,105",
        'table2': "12,200,107,243"
    }
    return render_template('resto_scheme.html', table_cords=table_cords)


@app.route('/resto/sсheme/table<int:table_num>')
def scheme(table_num):
    table = {
        1: 2,
        2: 4
    }
    date_now = datetime.datetime.now().date()
    time_now = datetime.datetime.now().strftime('%H:%M')
    date_stop = date_now + datetime.timedelta(365)

    return render_template('table.html',
                           table_num=table_num,
                           date_now=date_now,
                           date_stop=date_stop,
                           time_now=time_now,
                           max_people=table[table_num]
                           )


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
