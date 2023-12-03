import telebot

from loader import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    message_text = message
    bot.send_message(chat_id=message.from_user.id, text=message_text)


bot.polling(none_stop=True)
