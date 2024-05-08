from errno import errorcode
import psycopg2
import sys
import telebot
from telebot import types
import config

bot = telebot.TeleBot("1105513001:AAEW-P9_pVExBabcStfIKirDf525-nOoQgU")
admin = []
courier = [] # chat id  864159317
blok = []




try:
    db = psycopg2.connect(
    database="botdb",
    user="postgres",
    password="masha2552",
    host="127.0.0.1",
    port="5432"
     )

except psycopg2.Error as err:
     if err == errorcode.ER_ACCESS_DENIED_ERROR:
         print ("Что-то не так с вашим именем или паролем")
         sys.exit()
     elif err == errorcode.ER_BAD_DB_ERROR:
         print("База данных не существует")
         sys.exit()
     else:
          print(err)
          sys.exit()

cursor = db.cursor()

user_data = {}

class User:
     def __init__(self, first_name):
         self.first_name = first_name
         self.last_name = ''
         self.adress = ''
         self.phone = ''
         self.tovar = ''
         self.status = ''
         self.id = ''
         self.num = ''
         self.employee = ''

class Product:
    def __init__(self, name):
        self.name = name
        self.code_prod = ''
        self.price = ''
        self.pricerus = ''
        self.priсesng = ''

class Courier:
    def __init__(self, first_namec):
        self.first_name = first_namec
        self.last_namce = ''
        self.adressc = ''
        self.phonec = ''
class Rating:
    def __init__(self, id_courier):
        self.id_courier = id_courier
        self.ratings = ''

@bot.message_handler(commands=['start'], func=lambda message: message.chat.id in admin)
def welcomeadm(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Старт")
    item2 = types.KeyboardButton("Добавить товар")
    item3 = types.KeyboardButton("Обновить товар")
    item4 = types.KeyboardButton("Удалить товар")
    item5 = types.KeyboardButton("Добавить курьера")
    item6 = types.KeyboardButton("Обновить информацию о курьера")
    item7 = types.KeyboardButton("Уволить курьера")
    item8 = types.KeyboardButton("Добавить трек")
    item9 = types.KeyboardButton("Изменить статус")
    item10 = types.KeyboardButton("Назначить курьера")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8,item9,item10)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n<b>{1.first_name}</b> приветствует Вас - администратор.".format
                     (message.from_user, bot.get_me()),
                     reply_markup=markup, parse_mode='html' )

@bot.message_handler(commands=['start'], func=lambda message: message.chat.id in courier)
def welcomecour(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Старт")
    item2 = types.KeyboardButton("Внести трек-код")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n<b>{1.first_name}</b> приветствует Вас - курьер.".format
                     (message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['start'], func=lambda message: message.chat.id  in  blok)
def welcomeadm(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте, {0.first_name}!\nВладелец запретил Вам отвечать".format
                     (message.from_user, bot.get_me()), parse_mode='html')
@bot.message_handler(func=lambda message: message.chat.id in blok, content_types=['text'])
def exitingir (message):
    try:
        bot.send_message(message.chat.id, "Запрещено Вам отвечать!")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Старт")
    item2 = types.KeyboardButton("Оформить заказ")
    item3 = types.KeyboardButton("Просмотреть оформленые заказы")
    item4 = types.KeyboardButton("Просмотреть список товаров")
    item5 = types.KeyboardButton("Просмотреть последний заказ")
    item6 = types.KeyboardButton("Оценить работу курьера")
    markup.add(item1, item2,item3, item4, item5, item6)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n<b>{1.first_name}</b> - бот созданный чтобы принимать Ваши заказы.".format
                     (message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.chat.id in admin, content_types=['text'])
def admini(message):
    if message.chat.type == 'private':
        if message.text == 'Старт':
            welcomeadm(message)
        elif message.text == 'Добавить товар':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Product(message.text)
                msg = bot.send_message(message.chat.id, "Введите наименование тоовара")
                bot.register_next_step_handler(msg, process_namepro_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Удалить товар':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Product(message.text)
                msg = bot.send_message(message.chat.id, "Введите код товара")
                bot.register_next_step_handler(msg, process_delprod_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Добавить курьера':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Courier(message.text)
                msg = bot.send_message(message.chat.id, "Введите имя курьера")
                bot.register_next_step_handler(msg, process_cname_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Уволить курьера':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Courier(message.text)
                msg = bot.send_message(message.chat.id, "Введите имя курьера")
                bot.register_next_step_handler(msg, process_delcour_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Добавить трек':

            try:
                user_id = message.from_user.id
                user_data[user_id] = User(message.text)
                msg = bot.send_message(message.chat.id, "Введите номер заказа")
                bot.register_next_step_handler(msg, process_num_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Изменить статус':

            try:
                user_id = message.from_user.id
                user_data[user_id] = User(message.text)
                msg = bot.send_message(message.chat.id, "Введите номер заказа")
                bot.register_next_step_handler(msg, process_vipol_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Обновить товар':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Product(message.text)
                msg = bot.send_message(message.chat.id, "Введите наименование товара")
                bot.register_next_step_handler(msg, process_prodnew_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Обновить информацию о курьера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            clik1 = types.KeyboardButton("Изменить адрес")
            clik2 = types.KeyboardButton("Изменить телефон")
            markup.add(clik1, clik2)
            bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)
        elif message.text == 'Изменить адрес':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Courier(message.text)
                msg = bot.send_message(message.chat.id, "Введите имя курьера")
                bot.register_next_step_handler(msg, process_updcouriradress_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Изменить телефон':

            try:
                user_id = message.from_user.id
                user_data[user_id] = Courier(message.text)
                msg = bot.send_message(message.chat.id, "Введите имя курьера")
                bot.register_next_step_handler(msg, process_updcourirphone_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        elif message.text == 'Назначить курьера':

            try:
                user_id = message.from_user.id
                user_data[user_id] = User(message.text)
                msg = bot.send_message(message.chat.id, "Введите номер заказа")
                bot.register_next_step_handler(msg, process_emplo_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')

def process_emplo_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.id = message.text
        msg = bot.send_message(message.chat.id, "Введите идентификационный номер курьера")
        bot.register_next_step_handler(msg, process_emplo1_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_emplo1_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.employee = message.text
        sql = config.UPDIDCOUR
        val = ( user.employee, user.id,  )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о заказе обновлена")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_num_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.id = message.text
        msg = bot.send_message(message.chat.id, "Введите трек-код")
        bot.register_next_step_handler(msg, process_num1_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_num1_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.num = message.text
        sql = config.UPDNUM
        val = ( user.num, user.id,  )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о заказе обновлена")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_updcourirphone_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.first_namec = message.text
        msg = bot.send_message(message.chat.id, "Введите новый телефон")
        bot.register_next_step_handler(msg, process_updcourirphone1_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_updcourirphone1_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.phonec = message.text
        sql = config.UPDPHONEC
        val = (cour.phonec, cour.first_namec,)
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о курьере обновлена")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_updcouriradress_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.first_namec = message.text
        msg = bot.send_message(message.chat.id, "Введите новый адрес")
        bot.register_next_step_handler(msg, process_updcouriradress1_step)

    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_updcouriradress1_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.adressc = message.text
        sql = config.UPDADRESSC
        val = (cour.adressc, cour.first_namec, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о курьере обновлена")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_vipol_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.id = message.text
        msg = bot.send_message(message.chat.id, "Введите статус заказа")
        bot.register_next_step_handler(msg, process_vipol1_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_vipol1_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.status = message.text
        sql = config.UPDSTATUS
        val = (user.status, user.id,)
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о заказе обновлена")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_delcour_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.first_namec = message.text
        sql = config.DELCOURIER
        val = (cour.first_namec, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Курьер уволен")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_delprod_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.code_prod = message.text
        sql = config.DELPROD
        val = (product.code_prod, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Товар удален")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_prodnew_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.name = message.text
        msg = bot.send_message(message.chat.id, "Введите код товара")
        bot.register_next_step_handler(msg, process_prodnew1_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_prodnew1_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.code_prod = message.text
        sql = config.UPDPROD
        val = (product.code_prod, product.name, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Информация о товаре обновлена")

    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_namepro_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.name = message.text
        msg = bot.send_message(message.chat.id, "Введите код товара")
        bot.register_next_step_handler(msg, process_codepro_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_codepro_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.code_prod = message.text
        msg = bot.send_message(message.chat.id, "Введите стоимость товара")
        bot.register_next_step_handler(msg, process_pricepro_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_pricepro_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.price = message.text
        msg = bot.send_message(message.chat.id, "Введите стоимость доставки по России")
        bot.register_next_step_handler(msg, process_pricerusprod_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_pricerusprod_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.pricerus = message.text
        msg = bot.send_message(message.chat.id, "Введите стоимость доставки по СНГ")
        bot.register_next_step_handler(msg, process_pricesngprod_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_pricesngprod_step(message):
    try:
        user_id = message.from_user.id
        product = user_data[user_id]
        product.pricesng = message.text
        sql = "INSERT INTO product (name, code_prod, price, pricerus, pricesng) VALUES (%s, %s, %s, %s, %s)"
        val = (product.name, product.code_prod, product.price, product.pricerus, product.pricesng, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Новый товар добавлен")

    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_cname_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.first_namec = message.text
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_clname_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_clname_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.last_namec = message.text
        msg = bot.send_message(message.chat.id, "Введите адресс")
        bot.register_next_step_handler(msg, process_cadress_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_cadress_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.adressc = message.text
        msg = bot.send_message(message.chat.id, "Введите телефон")
        bot.register_next_step_handler(msg, process_cphone_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_cphone_step(message):
    try:
        user_id = message.from_user.id
        cour = user_data[user_id]
        cour.phonec = message.text
        sql = config.INSERTCOURIER
        val = (cour.first_namec,cour.last_namec, cour.adressc, cour.phonec, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Новый курьер добавлен")

    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

@bot.message_handler(func=lambda message: message.chat.id in courier, content_types=['text'])
def coureri(message):
    if message.chat.type == 'private':

        if message.text == 'Старт':
            welcomecour(message)
        elif message.text == 'Внести трек-код':
            try:
                user_id = message.from_user.id
                user_data[user_id] = User(message.text)
                msg = bot.send_message(message.chat.id, "Введите номер заказа")
                bot.register_next_step_handler(msg, process_num_step)
            except Exception as e:
                bot.reply_to(message, 'Ошибка!')
        else:
            bot.send_message(message.chat.id, 'Возникла ошибка!')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Старт':
        welcome(message)
    elif message.text == 'Оформить заказ':
        registrat(message)
    elif message.text == 'Просмотреть оформленые заказы':
        spisokzakaz(message)
    elif message.text == 'Просмотреть список товаров':
        spisoprod(message)
    elif message.text == 'Просмотреть последний заказ':
        posledzakaz(message)
    elif message.text == 'Оценить работу курьера':
        ocenka(message)

    else:
        bot.send_message(message.chat.id, 'Ошибка!')
def registrat(message):
    try:
        msg = bot.send_message(message.chat.id, "Введите имя")
        bot.register_next_step_handler(msg,process_firstname_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = User(message.text)
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_lastname_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def process_lastname_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.last_name = message.text
        msg = bot.send_message(message.chat.id, "Введите адресс")
        bot.register_next_step_handler(msg, process_adress_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def process_adress_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.adress = message.text
        msg = bot.send_message(message.chat.id, "Введите телефнон")
        bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
          bot.reply_to(message, 'Ошибка!')

def process_phone_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.phone = message.text
        msg = bot.send_message(message.chat.id, "Введите код товара")
        bot.register_next_step_handler(msg, process_tovar_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def process_tovar_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.tovar = message.text
        sql = "SELECT * FROM users WHERE user_id = {0}".format(user_id)
        cursor.execute(sql)
        existsUser = cursor.fetchone()
        if (existsUser == None):
            sql = config.INSERTUSERS
            val = (user_id, message.from_user.first_name, message.from_user.last_name)
            cursor.execute(sql, val)

        sql = config.INSERTREGS
        val = (user_id, user.first_name, user.last_name, user.adress, user.phone, user.tovar)
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Ваш заказ принят в обработку")
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def spisokzakaz(message):
    try:
        user_id = message.from_user.id
        sql = "SELECT * FROM regs WHERE user_id = {0}".format(user_id)
        cursor.execute(sql)
        spisok = cursor.fetchall()
        for inform in spisok:
            first_name = "Имя - {}".format(inform[2])
            last_name = "Фамилия - {}".format(inform[3])
            adress = "Адрес - {}".format(inform[4])
            phone = "Телефон - {}".format(inform[5])
            codepro = "Код товара - {}".format(inform[6])
            id_courier = "Код курьера - {}".format(inform[7])
            status = "Статус заказа - {}".format(inform[8])
            num = "Трек-код - {}".format(inform[9])
            ddate = "Дата оформления заказа - {}".format(inform[10])
            vse = ddate +'\n'+ first_name + '\n'\
                  + last_name +'\n' + adress + '\n'\
                  + phone + '\n' + codepro + '\n'+ id_courier + '\n'\
                  + status + '\n' + num
            bot.send_message(message.chat.id, vse)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')

def spisoprod(message):
    try:
        user_id = message.from_user.id
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        spisok = cursor.fetchall()
        for inform in spisok:
            name = "Наименование - {}".format(inform[1])
            code_prod = "Код товара - {}".format(inform[2])
            price = "Стоимость - {}".format(inform[3])
            pricerus = "Стоимость доставки по России - {}".format(inform[4])
            pricesng = "Стоимость доставки по СНГ - {}".format(inform[5])
            vse = name +'\n'+ code_prod + '\n'\
                  + price + '\n'+ pricerus + '\n'\
                  + pricesng
            bot.send_message(message.chat.id, vse)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def posledzakaz(message):
    try:
        user_id = message.from_user.id
        sql = "SELECT * FROM regs WHERE user_id = {0}".format(user_id)
        sql1 = "ORDER BY id DESC LIMIT 1"
        sql2 = sql +sql1
        cursor.execute(sql2)
        spisok = cursor.fetchall()
        for inform in spisok:
            first_name = "Имя - {}".format(inform[2])
            last_name = "Фамилия - {}".format(inform[3])
            adress = "Адрес - {}".format(inform[4])
            phone = "Телефон - {}".format(inform[5])
            codepro = "Код товара - {}".format(inform[6])
            id_courier = "Код курьера - {}".format(inform[7])
            status = "Статус заказа - {}".format(inform[8])
            num = "Трек-код - {}".format(inform[9])
            ddate = "Дата оформления заказа - {}".format(inform[10])
            vse = ddate + '\n' + first_name + '\n' \
                  + last_name + '\n' + adress + '\n' \
                  + phone + '\n' + codepro + '\n' + id_courier + '\n'\
                  + status + '\n' + num
            bot.send_message(message.chat.id, vse)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def ocenka(message):
    try:
        msg = bot.send_message(message.chat.id, "Введите код курьера")
        bot.register_next_step_handler(msg, process_oceniv_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_oceniv_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = Rating(message.text)
        msg = bot.send_message(message.chat.id, "Введите оценку 0-5")
        bot.register_next_step_handler(msg, process_ocenivanie_step)
    except Exception as e:
        bot.reply_to(message, 'Ошибка!')
def process_ocenivanie_step(message):
    try:
        user_id = message.from_user.id
        user = user_data[user_id]
        user.ratings = message.text
        sql = config.INSERTRAT
        val = (user.id_courier, user.ratings, )
        cursor.execute(sql, val)
        db.commit()
        bot.send_message(message.chat.id, "Ваша оценка добавлена")
        sql1 = config.SELECTAVG
        val1 = (user.id_courier,)
        cursor.execute(sql1, val1)
        spisok = cursor.fetchall()
        bot.send_message(message.chat.id, spisok)

    except Exception as e:
        bot.reply_to(message, 'Ошибка!')



if __name__ == '__main__':
    bot.polling(none_stop=True)