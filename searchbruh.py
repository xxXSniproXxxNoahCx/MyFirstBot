import random
from telegram.ext import Dispatcher,CommandHandler

def searching(update, context):
    Search = ["You searched the air and found some new unknown elements. You gained 300 XP. 你在空气里找到了一些新元素。你得到了 300 XP。", "YOU ROBBED THE BANK AND GAINED 120 XP. NOW RUN 你抢劫了银行并得到了 120 XP。快跑!!!!!", "You tried to rob the bank and got shot. Might need to learn how to play dodgeball next time. 你尝试去抢劫银行却被警察击中。下次练完躲避球再来吧。", "You begged on the street and got mistaken for a hobo. Did you forget that they don't give XP to beggers anymore? 你在路上讨钱。你忘了他们不再给讨钱的人 XP 了么？", "You searched the school and got mistaken for a kidnapper. You got jailed. 你搜索了学校但被误以为一个拐卖小孩的骗子。你入狱了。", "You searched the hospital, not konwing that it's a great mistake. You got covid 19 and died. 你搜索了医院，但被流感传染。你挂了。", "You searched the hospital and found a doctor's bag. You found a wallet with 20 XP inside. 你搜索了医院并找到了一名医生的包。你获得了 20 XP。", "You found 40 XP in the attic. How long had it been here? 你在阁楼找到了 40 XP。在这里待了多久了？", "You searched the haunted house and found a vault. You opened it and found 1000 XP! Luckily there was no ghosts inside 你搜索了鬼屋并找到了一个金库。你打开了它并找到了 1000 XP！幸好里面没有鬼。", "You searched a tree and found buried treasure worth 270 XP. GG! 你搜索了一棵树并找到了一批宝藏。你得到了 270 XP。 酷！", "You searched L - Park, not knowing it's a park for losers. Anyway, at least you got 9 XP from a bet with another kid. 你搜索了 L - 公园，最终收获了 9 XP。", "You searched the haunted house and got murdered by a ghost. Rip. 你尝试去搜索鬼屋。 你被 幽灵 给击败了。"]
    msg4 = random.choice(Search)
    msg4 += "\n\nAuthorised By Noah <3\n作者：Noah"
    update.message.reply_text(msg4)

def add_handler(dp:Dispatcher):
    search_handler = CommandHandler('search', searching)
    dp.add_handler(search_handler)



