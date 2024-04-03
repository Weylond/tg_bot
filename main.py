import telebot

bot = telebot.TeleBot('6574730390:AAGTnYkhJ5MoyframdqVuo3enjhRcaSaTEg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, Выбери свой знак зодиака')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Choose your problem with bot')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
