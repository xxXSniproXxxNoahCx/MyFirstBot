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
import bj

def start(update, context):
    update.message.reply_text("""

    Sup! My name is ᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ. Coded by O Great Noah.
    ᴅᴀɴᴋ ᴍᴇᴍᴇʀ ɪɪ provides a lot of fun features. You can do many things to try to get much XP as you want!
    
    You can also mess around with /DReward and /DPunish!
    Also, Noah will try to add some new feature really soon!
    
    Enjoy!
    
    --------------------
    Commands:
    
    /DReward: get daily rewards everyday!
    /DPunish: Don't get in trouble! 
    /DSearch: Be careful while scouting the area for XP!
    /DFish: hmm... I wonder what is down there under the sea...
    /DHunt: mess around with some animals and get some free XP! Beware of bears though...
    /DBeg: beg hobo...
    /DGuess (space bar and type a number from 0 - 100)! You can earn rewards!
    /DSolve [number] [add/subtract/multiply/divide] [number] gotta finish your math homework!
    /DBlackjack: First to 21...
    
    Hallo！！！我叫ᴅᴀɴᴋɪɪ。由伟大的 Noah创造。
    ᴅᴀɴᴋɪɪ 提供了许多有趣的功能。您可以做很多事情来尝试获得更多XP！
    
    你还可以四处乱搞。 
    
    此外，Noah会很快尝试添加一些新功能！
    
    玩得开心哦！
    
    --------------------
    指令：
    
    /DReward：获取每日奖励！
    /DPunish：别惹麻烦!
    /DSearch：搜寻XP区域时要小心！
    /DFish：嗯...我想知道海底有什么东西... 
    /DHunt： 狩猎一些动物，并获得一些免费的XP！请提防熊…… 
    /DBeg: 讨钱吧穷人
    /DGuess (空格 0～100里的一个数字）猜对了有奖励呦！
    /DSolve [数字1] [加/减/乘/除] [数字2] 回去做数学作业去！
    /DBlackjack: 二十一点
    --------------------
    """)

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
bj.add_handler(dispatcher)
guess.add_handler(dispatcher)
solve.add_handler(dispatcher)
updater.start_polling()
