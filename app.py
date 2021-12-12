from flask import Flask
from flask import render_template, request, flash, redirect, make_response

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


@app.route('/menu', methods=('GET', 'POST'))
def menu():
    order_list = {}
    menu_elements = {'pizza1': ['pizza1.png', 'Пицца Хэппи Хат', '529',
                                'Куриные фрикадельки в сочетании с брусничным соусом, сочный сладкий перец, томаты и нежный сыр Моцарелла'],
                     'pizza2': ['pizza2.jpg', 'Чизбургер', '729',
                                'Томатный соус, сыр Моцарелла, говядина, маринованые огурцы, красный лук, кетчуп, горчица Европейская'],
                     'pizza3': ['pizza3.png', 'Европейская', '629',
                                'Томатный соус, сыр Моцарелла, ветчина, грибы, помидоры'],
                     'pizza4': ['pizza4.png', 'Супер Суприм', '789',
                                'Соус Болоньезе, сыр Моцарелла, пепперони, курица, свинина, говядина, ветчина, зеленый перец, грибы, красный лук'],
                     'pizza5': ['pizza5.png', 'Супер Пепперони', '729', 'Томатный соус, сыр, экстра пепперони'],
                     'pizza6': ['pizza6.png', 'Гавайская', '629', 'Томатный соус, сыр Моцарелла, ветчина, ананасы'],
                     'pizza7': ['pizza7.png', 'Любители Овощей', '629',
                                'Томатный соус, сыр Моцарелла, грибы, сладкий перец, красный лук, томаты, маслины'],
                     'pizza8': ['pizza8.png', 'Пицца Чиззи Пури', '629',
                                'Пицца с сырами Сулугуни и Моцарелла на нежном сливочном соусе. Ближайший родственник знаменитой Хачапури!'],
                     'pizza9': ['pizza9.jpg', 'Супер Мясная Барбекю', '789',
                                'Соус Барбекю, сыр Моцарелла, сыр Чеддер, ветчина, бекон, пепперони, свинина, говядина, жареный лук'],
                     'pizza10': ['pizza10.jpg', 'Четыре Сыра', '729',
                                 'Томатный соус, сыры: Моцарелла, чеддер, сыр с голубой плесенью, Пармезан'],
                     'pizza11': ['pizza11.jpg', 'Любители Мяса', '729',
                                 'Томатный соус, сыр Моцарелла, пепперони, свинина, говядина, ветчина, бекон'],
                     'pizza12': ['pizza12.png', 'Итальянская', '629',
                                 'Томатный соус, сыр Моцарелла, ветчина, пепперони'],
                     'pizza13': ['pizza13.png', 'Супер Мясная', '789',
                                 'Соус Болоньезе, сыр Моцарелла, ветчина, бекон, пепперони, свинина, говядина'],
                     'pizza14': ['pizza14.jpg', 'Маргарита', '509', 'Томатный соус, сыр Моцарелла, помидоры'],
                     'pizza15': ['pizza15.jpg', 'Куриная Барбекю', '729',
                                 'Соус Барбекю, бекон, курица, красный лук, сладкий перец, грибы, сыр моцарелла, жареный лук']}

    if request.method == 'POST':
        pos = request.form['orderbtn']
        print(pos)
        if not request.cookies.get(str(pos)):
            res = make_response(render_template('menu_page.html', menu_elements=menu_elements))
            res.set_cookie(request.form['orderbtn'], '1')
        else:
            num = int(request.cookies.get(pos)) + 1
            res = make_response(render_template('menu_page.html', menu_elements=menu_elements))
            res.set_cookie(pos, str(num))
        return res

    return render_template('menu_page.html', menu_elements=menu_elements)


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
def qr_cod():
    if request.method == 'POST':
        return render_template('qr_page.html', STRING_TO_ENCODE=request.form['content'])
    return render_template('qr_page.html')


@app.route('/map')
def mapview():
    return render_template('maps_page.html')


@app.route('/tips')
def tips():
    return render_template('tips_page.html')


@app.route('/ofik')
def ofik():
    return render_template('ofik.html')


@app.route('/manager')
def manager():
    return render_template('manager.html')


@app.route('/pay', methods=('GET', 'POST'))
def pay():
    menu_elements = {'pizza1': ['pizza1.png', 'Пицца Хэппи Хат', '529',
                                'Куриные фрикадельки в сочетании с брусничным соусом, сочный сладкий перец, томаты и нежный сыр Моцарелла'],
                     'pizza2': ['pizza2.jpg', 'Чизбургер', '729',
                                'Томатный соус, сыр Моцарелла, говядина, маринованые огурцы, красный лук, кетчуп, горчица Европейская'],
                     'pizza3': ['pizza3.png', 'Европейская', '629',
                                'Томатный соус, сыр Моцарелла, ветчина, грибы, помидоры'],
                     'pizza4': ['pizza4.png', 'Супер Суприм', '789',
                                'Соус Болоньезе, сыр Моцарелла, пепперони, курица, свинина, говядина, ветчина, зеленый перец, грибы, красный лук'],
                     'pizza5': ['pizza5.png', 'Супер Пепперони', '729', 'Томатный соус, сыр, экстра пепперони'],
                     'pizza6': ['pizza6.png', 'Гавайская', '629', 'Томатный соус, сыр Моцарелла, ветчина, ананасы'],
                     'pizza7': ['pizza7.png', 'Любители Овощей', '629',
                                'Томатный соус, сыр Моцарелла, грибы, сладкий перец, красный лук, томаты, маслины'],
                     'pizza8': ['pizza8.png', 'Пицца Чиззи Пури', '629',
                                'Пицца с сырами Сулугуни и Моцарелла на нежном сливочном соусе. Ближайший родственник знаменитой Хачапури!'],
                     'pizza9': ['pizza9.jpg', 'Супер Мясная Барбекю', '789',
                                'Соус Барбекю, сыр Моцарелла, сыр Чеддер, ветчина, бекон, пепперони, свинина, говядина, жареный лук'],
                     'pizza10': ['pizza10.jpg', 'Четыре Сыра', '729',
                                 'Томатный соус, сыры: Моцарелла, чеддер, сыр с голубой плесенью, Пармезан'],
                     'pizza11': ['pizza11.jpg', 'Любители Мяса', '729',
                                 'Томатный соус, сыр Моцарелла, пепперони, свинина, говядина, ветчина, бекон'],
                     'pizza12': ['pizza12.png', 'Итальянская', '629',
                                 'Томатный соус, сыр Моцарелла, ветчина, пепперони'],
                     'pizza13': ['pizza13.png', 'Супер Мясная', '789',
                                 'Соус Болоньезе, сыр Моцарелла, ветчина, бекон, пепперони, свинина, говядина'],
                     'pizza14': ['pizza14.jpg', 'Маргарита', '509', 'Томатный соус, сыр Моцарелла, помидоры'],
                     'pizza15': ['pizza15.jpg', 'Куриная Барбекю', '729',
                                 'Соус Барбекю, бекон, курица, красный лук, сладкий перец, грибы, сыр моцарелла, жареный лук']}

    sum_pizza = 0
    for pizza in menu_elements:
        if request.cookies.get(pizza):
            sum_pizza += int(menu_elements[pizza][2]) * int(request.cookies.get(pizza))

    if request.method == 'POST':
        print(request.form['paybtn'])
        if request.form['paybtn'] == "Pay":
            res = make_response(render_template('pay_page.html', sum_pizza="0"))
            for pizza in menu_elements:
                if request.cookies.get(pizza):
                    res.set_cookie(pizza, '0', max_age=0)
            return res

    return render_template('pay_page.html', sum_pizza=str(sum_pizza))
