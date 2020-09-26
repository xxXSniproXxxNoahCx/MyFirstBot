import random
from telegram.ext import Dispatcher,CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import os
import rewardbruh
import punishbruh
import fishbruh
import searchbruh
import huntbruh

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Sup. My Name is Snipro XP Bot. \n Type /rw to get an reward 奖励, \n/pn to get a punishment 惩罚, \n/sr to search 搜索, \n/ht to hunt 捕猎, \nand /fs to fish 钓鱼! \nEnjoy!")

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
fishbruh.add_handler(dispatcher)
searchbruh.add_handler(dispatcher)
huntbruh.add_handler(dispatcher)
updater.start_polling()
