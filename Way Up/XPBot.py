import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
 
def rewarded(update, context):
    reward = ["Yay you got 200 XP. Cool?", "You got 50 XP.", "You got Nothing. Git Gud."]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(reward))

def punish(update, context):
    punished = ["You lost 20 hp for not behaving well.", "You died. You lost 80 hp.", "You dodged and didn't get punished."]
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(punished))

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

reward_handler = CommandHandler('rw', rewarded)

punishment_handler = CommandHandler('pn', punish)

dispatcher.add_handler(reward_handler)
dispatcher.add_handler(punishment_handler)

updater.start_polling()
