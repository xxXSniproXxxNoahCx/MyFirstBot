import random
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler

n = random.randint(1,99)
tries = 0
def guessing(update, context):
  global n
  global tries
  user = update.message.from_user
  msg8 = ""
  gn = "猜一个0-100之间的数字。\nGuess a number from 0 - 100.\n\nLeaderboards: %s - %s\n "%(user.username,tries)
  b = context.args[0]
  a = int(b)
  msg8 += gn
  if a == n :
    tries = tries + 1
    msg8 += "Ayyy You guessed it! You guessed it in %s tries. 天呐你竟然猜到了 概率是 %%1 呀！ 500 XP 你值得拥有。竟然 %s 次就猜到了."%(tries,tries) 
    n = random.randint(1,99)
    tries = 0
  elif a > n :
    tries = tries + 1
    msg8 += "大了！重猜！It's too big! Guess again!"
  elif a < n :
    tries = tries + 1
    msg8 += "小了！重猜！It's too small! Guess again!"
  elif a != int :
    tries = tries + 1
    msg8 += "想什么呢审题呀 ur bad thats not a number"
  msg8 += "\nTRIES: %s\n\nAuthorised By Noah <3\n作者：Noah"%(tries)
  update.message.reply_text(msg8)

def add_handler(dp:Dispatcher):
  guess_handler = CommandHandler('guess',guessing)
  dp.add_handler(guess_handler)