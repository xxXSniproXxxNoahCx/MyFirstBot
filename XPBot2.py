import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import os
import rewardbruh
import punishbruh

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Sup. My Name is Snipro XP Bot.")

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN = read_file_as_str('TOKEN2')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
rewardbruh.add_handler(dispatcher)
punishbruh.add_handler(dispatcher)
updater.start_polling()
