import random
from telegram.ext import Dispatcher,CommandHandler, ConversationHandler

def guessing(update, context):
  msg8 = ""
  n = random.randint(1,9)
  gn = "You guessed a number from 0 - 10. "
  b = update.message.text
  a = int(b.split()[1])
  print(a)
  msg8 += gn
  if a == n :
    msg8 += "Ayyy You guessed it! You got 500 XP for your price."   
  elif a == n - 1 or a == n + 1 :
    msg8 += "Yikes Almost!!!! 100 XP CUZ I FEEL BAD for u. Correct answer is %s."%(n)
  elif a > n - 1 or a < n + 1 :
    msg8 += "Wrong! The correct answer is %s"%(n)
  elif a != int :
    msg8 += "ur bad thats not a number"
  update.message.reply_text(msg8)



def add_handler(dp:Dispatcher):
    guess_handler = CommandHandler('guess',guessing)
    dp.add_handler(guess_handler)





