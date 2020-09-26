import random
from telegram.ext import Dispatcher,CommandHandler

def fish(update, context):
    Fish = ["LOL You got nothing, git gud. 哈哈哈钓了一天鱼都没钓着。回家修炼去吧！", "You brought one common fish and gained 5 XP! 你钓到了一条 太阳鱼 ，收获了 5 XP。", "You brought back two common fishes and gained 10 XP! 你钓到了两条 太阳鱼 ，收获了 10 XP。", "You brought back four common fishes and gained 20 XP! 你钓到了四条 太阳鱼 ，收获了 20 XP。", "You brought back one RARE fish and gained 100 XP! Whoo Hoo! 你钓到了一条 大嘴鲈鱼 ，收获了 100 XP。棒棒哒～ ", "You fished up a credit card and gave it to the police. You gained 700 XP. Wait what just happened? 你钓到一张银行卡并交给了警察。你得到了 700 XP。等会等会，发生了什么?!"]
    msg3 = random.choice(Fish)
    msg3 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg3)

def add_handler(dp:Dispatcher):
    fish_handler = CommandHandler('DFish', fish)
    dp.add_handler(fish_handler)

