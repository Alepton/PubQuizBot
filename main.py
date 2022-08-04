import telebot
from telebot import types


bot = telebot.TeleBot('5214067093:AAE0oaamKHPoIV5wNxpssNVDoXiWpn-u5JM')

# основаная клавиатура
def create_keyboard_main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Создать вопрос', callback_data='main_1')
    btn2 = types.InlineKeyboardButton(text='Редактировать вопрос', callback_data='main_2')
    btn3 = types.InlineKeyboardButton(text='Опубликовать вопрос', callback_data='main_3')
    markup.add(btn1, btn2, btn3)
    return markup


def keyboard_create_quiz():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Добавить текст вопроса', callback_data='quiz_1')
    btn2 = types.InlineKeyboardButton(text='Добавить картинку к вопросу', callback_data='quiz_2')
    btn3 = types.InlineKeyboardButton(text='Добавить вариант ответа', callback_data='quiz_3')
    btn4 = types.InlineKeyboardButton(text='Добавить правильный вариант ответа', callback_data='quiz_4')
    markup.add(btn1, btn2, btn3, btn4)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    markup = create_keyboard_main()
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nВыбери что ты хочешь сделать"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup = keyboard_create_quiz()
    if call.message:
        if call.data == 'main_1':
            bot.send_message(call.message.chat.id, 'Переходим к созданию вопроса', reply_markup=markup)
        if call.data == 'main_2':
            bot.send_message(call.message.chat.id, 'Корректируем вопрос', reply_markup=markup)
        if call.data == 'main_3':
            bot.send_message(call.message.chat.id, 'Публикуем вопрос', reply_markup=markup)
    #print(call.data)
    #print(call.message)

quiz = {}

def creat_text():
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_quiz(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Сохранить', callback_data='21')
    markup.add(btn1, )
    if call.message:
        if call.data == 'quiz_1':
            bot.send_message(call.message.chat.id, 'Отправьте ваш вопрос а потом нажмите кнопку ниже', reply_markup=markup)
        if call.data == 'quiz_2':
            pass
        if call.data == 'quiz_3':
            pass
        if call.data == 'quiz_4':
            pass
    print(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)