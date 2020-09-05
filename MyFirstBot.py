from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
text="Sup. My Name is Snipro Bot.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

updater = Updater(token='1377719938:AAGmIcuWsMMpPw0vejQpLPQvaGs24_8ovGM', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)

dispatcher.add_handler(echo_handler)

updater.start_polling()
