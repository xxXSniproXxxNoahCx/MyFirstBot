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
import beg
import guess

def start(update, context):
    update.message.reply_text("Sup! My name is ᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ. Coded by O Great Noah.\nᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ provides a lot of fun features. You can do many things to try to get much XP as you want!\n\nYou can also mess around with /reward and /punish!\nAlso, Noah will try to add some new feature really soon!\n\nEnjoy!\n\n--------------------\nCommands:\n\n/reward: get daily rewards!\n/punish: Don't get in trouble! \n/search: Be careful while scouting the area for XP!\n/fish: hmm... I wonder what is down there under the sea...\n/hunt: mess around with some animals and get some free XP! Beware of bears though...\n/beg: beg hobo...\n/guess (space bar and type a number from 0 - 10)! You can earn rewards!\n\n Hallo！！！我叫ᴅᴀɴᴋɪɪ。由伟大的 Noah创造。\n ᴅᴀɴᴋɪɪ 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！\n\n你还可以四处乱搞。 \n\n此外，Noah会很快尝试添加一些新功能！\n\n玩得开心哦！\n\n--------------------\n指令：\n\n /reward：获取每日奖励！\n/punish：别惹麻烦!\n/search：搜寻XP区域时要小心！\n/fish：嗯...我想知道海底有什么东西... \n/hunt： 狩猎一些动物，并获得一些免费的XP！请提防熊…… \n/beg: 讨钱吧穷人\n/guess (空格 0～10里的一个数字）猜对了有奖励呦！\n\n--------------------")

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
beg.add_handler(dispatcher)
rewardbruh.add_handler(dispatcher)
punishbruh.add_handler(dispatcher)
fishbruh.add_handler(dispatcher)
searchbruh.add_handler(dispatcher)
huntbruh.add_handler(dispatcher)
guess.add_handler(dispatcher)
updater.start_polling()
