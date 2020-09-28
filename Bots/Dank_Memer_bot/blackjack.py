import random
from telegram.ext import Dispatcher,CommandHandler,ConversationHandler

sc = int(random.randint(1,20))

msg99999 = ("Blackjack\n\nFirst to 21. You start on %s. If you wish to hit, type '/dblackjack h'. If you wish to save, type '/dblackjack s'."%(sc))
msg88888 = ""
def bjhelp():
  return """ 
    二十一点
规则：

开始之后，系统会随机生成 2 个 1 到 20 之间的数字。一的是你的起点点数，一个是对手的。
如果你的点数超过 21 或者你的点数比对手小，你将输掉此赌注。
如果你的点数等于 21 或者你的点数比对手大，你将赢得此赌注。

If you wish to hit, type '/dblackjack h'. If you wish to save, type '/dblackjack s'.
To start, type '/dstartbj'.
    """

def start(update, context):
    global msg99999
    update.message.reply_text(msg99999)
def blackjacking(update, context):
    global msg99999
    global msg88888
    global sc
    ri = random.randint(500,1500)
    rc = int(random.randint(1,11))
    osc = int(random.randint(1,20))
    bb = update.message.text
    hit = "h"
    save = "s"
    print(bb)
    if len(context.args) == 0 :
        update.message.reply_text(bjhelp())
        return 
    bjc = context.args[0]
    if bjc == hit:
        if rc == 11 and sc + rc > 21:
            sc += 1
        else:
            sc += rc
        if sc < osc or sc > 21:
            msg88888 += "You lost the bet. Your number is %s, Opponent number is %s. You lost the XP you betted."%(sc,osc)
            sc = 0
        elif sc > osc and sc <= 21:
            msg88888 += "\n\nYou won the blackjack! Your number is %s, Opponent number is %s. You betted %s XP (I don't care if its not right), so your reward is %s XP!"%(sc,osc,ri,ri*2)
            sc = 0
        elif sc == osc :
            msg88888 += "You didn't lose nor win anything. L?"
            sc = 0
    elif bjc == save:
        if sc < osc or sc > 21:
            msg88888 += "You lost the bet. Your number is %s, Opponent number is %s. You lost the XP you betted."%(sc,osc)
            sc = 0
        elif sc > osc and sc <= 21:
            msg88888 += "\n\nYou won the blackjack! Your number is %s, Opponent number is %s. You betted %s XP (I don't care if its not right), so your reward is %s XP!"%(sc,osc,ri,ri*2)
            sc = 0
        elif sc == osc :
            msg88888 += "You didn't lose nor win anything. L?"
            sc = 0
    update.message.reply_text(msg88888)
 

def add_handler(dp:Dispatcher):
    blackjack_handler = CommandHandler('DBlackjack', blackjacking)
    bjs_handler = CommandHandler("DStartBj", start)
    dp.add_handler(blackjack_handler)
    dp.add_handler(bjs_handler)





