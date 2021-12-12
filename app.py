from flask import Flask
from flask import render_template, request, flash, redirect


from flask_qrcode import QRcode


import datetime

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
    menu_elements = {'pizza1': ['static/img/pizza1.png', 'Пицца Хэппи Хат', '529', 'Куриные фрикадельки в сочетании с брусничным соусом, сочный сладкий перец, томаты и нежный сыр Моцарелла'],
                     'pizza2': ['static/img/pizza2.jpg', 'Чизбургер', '729', 'Томатный соус, сыр Моцарелла, говядина, маринованые огурцы, красный лук, кетчуп, горчица Европейская'],
                     'pizza3': ['static/img/pizza3.png', 'Европейская', '629', 'Томатный соус, сыр Моцарелла, ветчина, грибы, помидоры']}
    return render_template('menu_page.html')


@app.route('/resto/scheme_<rest_name>')
def scheme2(rest_name=None):
    table_cords = {
        'table1': "10,50,70,105",
        'table2': "150,55,210,110",
        'table3': "12,200,110,245",
        'table4': "45,320,90,415",

        'table5': "270,10,330,70",
        'table6': "235,135,300,190",
        'table7': "280,250,340,310",

        'table8': "385,120,480,165",
        'table9': "385,230,480,285",
        'table10': "650,410,750,455",

        'table11': "560,35,745,350",

        'table12': "390,510,440,615",
        'table13': "520,510,570,615",
        'table14': "650,510,700,615",


    }
    return render_template('resto_scheme.html', table_cords=table_cords, rest_name=rest_name)


@app.route('/resto/sсheme_<rest_name>/table<int:table_num>')
def scheme(rest_name, table_num):
    table = {
        1: 2,
        2: 4,
        3: 4,
        4: 4,
        5: 2,
        6: 2,
        7: 2,
        8: 4,
        9: 4,
        10: 4,
        11: 1,
        12: 4,
        13: 4,
        14: 4
    }
    date_now = datetime.datetime.now().date()
    time_now = datetime.datetime.now().strftime('%H:%M')
    date_stop = date_now + datetime.timedelta(365)

    return render_template('table.html',
                           rest_name=rest_name,
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
    return render_template('maps_page.html')


@app.route('/tips')
def tips():
    return render_template('tips_page.html')
