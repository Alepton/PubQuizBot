import telebot
from telebot import types


bot = telebot.TeleBot('5214067093:AAE0oaamKHPoIV5wNxpssNVDoXiWpn-u5JM')

# основаная клавиатура
def create_keyboard_main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Создать вопрос', callback_data='1')
    btn2 = types.InlineKeyboardButton(text='Редактировать вопрос', callback_data='2')
    btn3 = types.InlineKeyboardButton(text='Опубликовать вопрос', callback_data='3')
    markup.add(btn1, btn2, btn3)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_keyboard()
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nВыбери что ты хочешь сделать"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup = create_keyboard_main()
    if call.message:
        if call.data == '1':
            bot.send_message(call.message.chat.id, 'Переходим к созданию вопроса', reply_markup=markup)
        if call.data == '2':
            bot.send_message(call.message.chat.id, 'Корректируем вопрос', reply_markup=markup)
        if call.data == '3':
            bot.send_message(call.message.chat.id, 'Публикуем вопрос', reply_markup=markup)
    #print(call.data)
    #print(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)