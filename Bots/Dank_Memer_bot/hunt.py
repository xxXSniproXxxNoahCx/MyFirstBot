import random
from telegram.ext import Dispatcher,CommandHandler

def hunting(update, context):
    Hunt = ["LOL you suck, you found nothing to hunt 哈哈你没有找到任何东西去捕猎", "LOL you suck, you found nothing to hunt 哈哈你没有找到任何东西去捕猎", "LOL you suck, you found nothing to hunt 哈哈你没有找到任何东西去捕猎", "A bear ate you. You died. 一只熊把你吃掉了", "A bear ate you. You died. 一只熊把你吃掉了", "You brought back a skunk and gained 10 XP! 你拿回来一只臭鼬并收获了 10 XP！", "You brought back a skunk and gained 10 XP 你拿回来一只臭鼬并收获了 10 XP！!", "You brought back a rabbit and gained 15 xp! 你拿回来一只兔子并收获了 15 XP！", "You brought back a rabbit and gained 15 XP! 你拿回来一只兔子并收获了 15 XP！",  "You brought back a rabbit and gained 15 xp! 你拿回来一只兔子并收获了 15 XP！", "You brought back a duck and gained 25 xp! 你拿回来一只鸭子并收获了 25 XP", "You brought back a duck and gained 25 xp! 你拿回来一只鸭子并收获了 25 XP！", "You brought back a boar and gained 70 xp! 你拿回来一只野猪并收获了 70 XP！", "Holy Moly! You brought back a DRAGON and gained 400 XP! How'd you even manage that? 我哩个天呐！你拿回来了一只龙并收获了 400 XP！你是咋么做到的？"]
    msg5 = random.choice(Hunt)
    msg5 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg5)

def add_handler(dp:Dispatcher):
    hunt_handler = CommandHandler('DHunt', hunting)
    dp.add_handler(hunt_handler)





