import random
from telegram.ext import Dispatcher,CommandHandler

def rewarded(update, context):
    reward = ["Yay you got 200 XP. Cool? 你收获了 200 XP。棒棒哒~ ", "You got 50 XP. 你获得了 50 XP。", "You got Nothing. Git Gud. 你一无所成。再修炼100年吧～ ", "Let God decide. 让神决定你的命运吧。 \nYou got lucky dunky! God has gifted you %s XP. 你的幸运终于来了！神给予了你 （上面英文版写了，懒得再写一遍了） XP。"%(random.randint(100,250))]
    msg = random.choice(reward)
    msg += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg)

def add_handler(dp:Dispatcher):
    reward_handler = CommandHandler('reward', rewarded)
    dp.add_handler(reward_handler)

