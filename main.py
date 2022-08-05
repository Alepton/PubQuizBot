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

def keyboard_add_text():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Сохранить вопрос', callback_data='text_1')
    markup.add(btn1, )
    return markup

def save_question():
    @bot.message_handler(content_types=["text"])
    def repeat_messages(message):  # Название функции не играет никакой роли
        markup = keyboard_add_text()
        bot.send_message(message.chat.id, message.text, reply_markup=markup)

        print(message.id)



@bot.message_handler(commands=['start'])
def start(message):
    markup = create_keyboard_main()
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nВыбери что ты хочешь сделать"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


# функция ожидает колбэки и выполняется при их наличии
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup_quiz = keyboard_create_quiz()
    markup_text = keyboard_add_text()

    if call.message:
        if call.data == 'main_1':
            bot.send_message(call.message.chat.id, 'Переходим к созданию вопроса', reply_markup=markup_quiz)
        if call.data == 'main_2':
            bot.send_message(call.message.chat.id, 'Корректируем вопрос', reply_markup=markup_quiz)
        if call.data == 'main_3':
            bot.send_message(call.message.chat.id, 'Публикуем вопрос', reply_markup=markup_quiz)
        if call.data == 'quiz_1':
            bot.send_message(call.message.chat.id, 'Отправьте ваш вопрос а потом нажмите кнопку ниже')
            save_question()
        if call.data == 'text_1':
            bot.send_message(call.message.chat.id, 'Вопрос принят', reply_markup=markup_quiz)
            print(call.message.text)
    #print(call.data)


quiz_text = ''
quiz_description = ''
quiz_answer = []
quiz_img = ''


def creat_text():
    pass



if __name__ == '__main__':
    bot.polling(none_stop=True)