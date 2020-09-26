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
import solve

def start(update, context):
    update.message.reply_text("Sup! My name is ᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ. Coded by O Great Noah.\nᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ provides a lot of fun features. You can do many things to try to get much XP as you want!\n\nYou can also mess around with /DReward and /DPunish!\nAlso, Noah will try to add some new feature really soon!\n\nEnjoy!\n\n--------------------\nCommands:\n\n/DReward: get daily rewards everyday!\n/DPunish: Don't get in trouble! \n/DSearch: Be careful while scouting the area for XP!\n/DFish: hmm... I wonder what is down there under the sea...\n/DHunt: mess around with some animals and get some free XP! Beware of bears though...\n/DBeg: beg hobo...\n/DGuess (space bar and type a number from 0 - 100)! You can earn rewards!\n/DSolve [number] [add/subtract/multiply/divide] [number] gotta finish your math homework!\n\nHallo！！！我叫ᴅᴀɴᴋɪɪ。由伟大的 Noah创造。\nᴅᴀɴᴋɪɪ 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！\n\n你还可以四处乱搞。 \n\n此外，Noah会很快尝试添加一些新功能！\n\n玩得开心哦！\n\n--------------------\n指令：\n\n /DReward：获取每日奖励！\n/DPunish：别惹麻烦!\n/DSearch：搜寻XP区域时要小心！\n/DFish：嗯...我想知道海底有什么东西... \n/DHunt： 狩猎一些动物，并获得一些免费的XP！请提防熊…… \n/DBeg: 讨钱吧穷人\n/DGuess (空格 0～100里的一个数字）猜对了有奖励呦！\n/DSolve [数字1] [加/减/乘/除] [数字2] 回去做数学作业去！\n\n--------------------")

def read_file_as_str(file_path): 
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

TOKEN = read_file_as_str('TOKEN2')
print (TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('DStart', start)
info_handler = CommandHandler('DInfo', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
beg.add_handler(dispatcher)
rewardbruh.add_handler(dispatcher)
punishbruh.add_handler(dispatcher)
fishbruh.add_handler(dispatcher)
searchbruh.add_handler(dispatcher)
huntbruh.add_handler(dispatcher)
guess.add_handler(dispatcher)
solve.add_handler(dispatcher)
updater.start_polling()
