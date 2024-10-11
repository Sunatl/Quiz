import telebot
from secret import telebotsssss
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot(telebotsssss, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    bnt1 = InlineKeyboardButton("/Savoli_1")
    bnt2 = InlineKeyboardButton("/Savoli_2")
    bnt3 = InlineKeyboardButton("/Savoli_3")
    bnt4 = InlineKeyboardButton("/Savoli_4")
    bnt5 = InlineKeyboardButton("/Savoli_5")
    maskur.add(bnt1, bnt2, bnt3, bnt4, bnt5)
    
    bot.send_message(message.chat.id, f"Хуш омадед! Akai {message.chat.username} ба боти аввалини ман. Шумо мехохед ботсозиро дар забони python йод гиред пас  дарси 1 ро пахш кунед!", reply_markup=maskur)


@bot.message_handler(commands=['Savoli_1'])
def darsi_1(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Corect1")
    bnt2 = InlineKeyboardButton("/Wrong1")
    maskur.add(bnt1, bnt2)
    bot.send_message(message.chat.id, """
1. Агар як адади мусбат бо як адади манфӣ ҷамъ карда шавад ва натиҷа манфӣ бошад, оё ин маънои онро дорад, ки ҳар гуна ҷамъи ду адади мусбату манфӣ ҳатман манфӣ хоҳад буд?
""",reply_markup=maskur
)

@bot.message_handler(commands=['Savoli_2'])
def darsi_2(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Corect2")
    bnt2 = InlineKeyboardButton("/Wrong2")
    maskur.add(bnt1, bnt2)
    bot.send_message(message.chat.id, """
2. Агар як адади мураккаб ба ҳосили зарби ду адади мусбат баробар бошад, оё ин маънои онро дорад, ки ин адади мураккаб ҳатман ба як адади мусбат баробар аст?
""",reply_markup=maskur)

@bot.message_handler(commands=['Savoli_3'])
def darsi_3(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Corect3")
    bnt2 = InlineKeyboardButton("/Wrong3")
    maskur.add(bnt1, bnt2)

    bot.send_message(message.chat.id, """
Оё ҳар як адади натуралӣ ба таври қатъӣ зарурати доштани рақам дар системаи дуӣ дорад?
""",reply_markup=maskur)

@bot.message_handler(commands=['Savoli_4'])
def darsi_4(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Corect4")
    bnt2 = InlineKeyboardButton("/Wrong4")
    maskur.add(bnt1, bnt2)
    bot.send_message(message.chat.id, """
Агар шумо рақами ягон адади натуралиро чандин маротиба ба худ зарб кунед, оё натиҷа ҳамеша аз рақами аслии он бузургтар мешавад?
""",reply_markup=maskur)

@bot.message_handler(commands=['Savoli_5'])
def darsi_5(message):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Corect5")
    bnt2 = InlineKeyboardButton("/Wrong5")
    maskur.add(bnt1, bnt2)
    bot.send_message(message.chat.id, """
Агар ду адади мусбат 𝑎 ва 𝑏дошта бошем, ва агар 𝑎>𝑏,оё 𝑎**3>𝑏**3низ ҳамеша дуруст аст?
""")
    
   
   
   
    
# savoli 111111111111111
@bot.message_handler(commands=['Corect1'])
def corect1(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes1")
    bnt2 = InlineKeyboardButton("/No1")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Bubakhshed akai {massage.chat.username} gavobi guftai shumo khato hast!Mekhohed gavobro bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Wrong1'])
def wrong1(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes1")
    bnt2 = InlineKeyboardButton("/No1")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Javobi shumo durust akai {massage.chat.username}.Mekhohed gavobro purra bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Yes1'])
def yes1(massage):
    bot.send_message(massage.chat.id,"Ҷавоб: Не, агар як адади мусбат бо як адади манфӣ ҷамъ карда шавад ва натиҷа манфӣ бошад, пас ин маънои онро надорад, ки ҳар гуна ҷамъи ду адади мусбату манфӣ ҳатман манфӣ хоҳад буд. Зеро ҷамъи ду адади мусбату манфӣ метавонад ҳам мусбат, ҳам манфӣ ва ҳатто сифр ҳам бошад, вобаста ба андозаи ин ададҳо.In bud gavobi mo baroi savolhoi digaro khondan tumai /start zer kuned")

@bot.message_handler(commands=['No1'])
def No1(massage):
    bot.send_message(massage.chat.id,"Bashumo muvafakiyat agar khohed davom dihed pass tugmai /start ro zer kuned")







# savoli 222222222222222222
@bot.message_handler(commands=['Corect2'])
def corect2(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes2")
    bnt2 = InlineKeyboardButton("/No2")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Bubakhshed akai {massage.chat.username} gavobi guftai shumo khato hast!Mekhohed gavobro bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Wrong2'])
def wrong2(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes2")
    bnt2 = InlineKeyboardButton("/No2")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Javobi shumo durust akai {massage.chat.username}.Mekhohed gavobro purra bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Yes2'])
def yes2(massage):
    bot.send_message(massage.chat.id,"Ҷавоб: Не, агар як адади мураккаб ба ҳосили зарби ду адади мусбат баробар бошад, пас ин маънои онро надорад, ки ин адади мураккаб ҳатман ба як адади мусбат баробар аст. Зеро адади мураккаб метавонад ҳосили зарби ду адади мусбат бошад, вале худаш бо як адади мусбат баробар набошад.In bud gavobi mo baroi savolhoi digaro khondan tumai /start zer kuned")

@bot.message_handler(commands=['No2'])
def No2(massage):
    bot.send_message(massage.chat.id,"Bashumo muvafakiyat agar khohed davom dihed pass tugmai /start ro zer kuned")








# savoli 3333333333333333333333
@bot.message_handler(commands=['Corect3'])
def corect3(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes3")
    bnt2 = InlineKeyboardButton("/No3")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Javobi shumo durust akai {massage.chat.username}.Mekhohed gavobro purra bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Wrong3'])
def wrong3(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes3")
    bnt2 = InlineKeyboardButton("/No3")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Bubakhshed akai {massage.chat.username} gavobi guftai shumo khato hast!Mekhohed gavobro bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Yes3'])
def yes3(massage):
    bot.send_message(massage.chat.id,"Ҷавоб: Бале, ҳар як адади натуралӣ метавонад бо системаи дуӣ навишта шавад, зеро ин як усули умумии рақамгузории ададҳо аст, ки танҳо 0 ва 1-ро истифода мебарад.In bud gavobi mo baroi savolhoi digaro khondan tumai /start zer kuned")

@bot.message_handler(commands=['No3'])
def No3(massage):
    bot.send_message(massage.chat.id,"Bashumo muvafakiyat agar khohed davom dihed pass tugmai /start ro zer kuned")








# savoli 444444444444444444444
@bot.message_handler(commands=['Corect4'])
def corect4(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes4")
    bnt2 = InlineKeyboardButton("/No4")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Bubakhshed akai {massage.chat.username} gavobi guftai shumo khato hast!Mekhohed gavobro bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Wrong4'])
def wrong4(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes4")
    bnt2 = InlineKeyboardButton("/No4")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Javobi shumo durust akai {massage.chat.username}.Mekhohed gavobro purra bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Yes4'])
def yes4(massage):
    bot.send_message(massage.chat.id,"""Ҷавоб: Не, агар шумо рақамҳои манфӣ ё ададҳои хурдтар аз 1-ро ба назар гиред, натиҷа ҳамеша аз рақами аслии он бузургтар намешавад. Масалан, 
0.5×0.5=0.25.
In bud gavobi mo baroi savolhoi digaro khondan tumai /start zer kuned""")

@bot.message_handler(commands=['No4'])
def No4(massage):
    bot.send_message(massage.chat.id,"Bashumo muvafakiyat agar khohed davom dihed pass tugmai /start ro zer kuned")



# savoli 555555555555555555555555555555
@bot.message_handler(commands=['Corect5'])
def corect5(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes5")
    bnt2 = InlineKeyboardButton("/No5")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Javobi shumo durust akai {massage.chat.username}.Mekhohed gavobro purra bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Wrong5'])
def wrong5(massage):
    maskur = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bnt1 = InlineKeyboardButton("/Yes5")
    bnt2 = InlineKeyboardButton("/No5")
    maskur.add(bnt1, bnt2)
    bot.send_message(massage.chat.id,f"""Bubakhshed akai {massage.chat.username} gavobi guftai shumo khato hast!Mekhohed gavobro bined
    """,reply_markup=maskur)

@bot.message_handler(commands=['Yes5'])
def yes5(massage):
    bot.send_message(massage.chat.id,"""Ҷавоб: Бале, агар 𝑎>𝑏, пас 𝑎**3>𝑏**3
, зеро зарби ҳарду адад мусбат аст ва куб низ ин бузургиро ҳифз мекунад.
.In bud gavobi mo baroi savolhoi digaro khondan tumai /start zer kuned""")
    
    
    
@bot.message_handler(commands=['No5'])
def No5(massage):
    bot.send_message(massage.chat.id,"Bashumo muvafakiyat agar khohed davom dihed pass tugmai /start ro zer kuned")
bot.infinity_polling()