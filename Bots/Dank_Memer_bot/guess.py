import random
from telegram.ext import Dispatcher, CommandHandler, ConversationHandler
# n = random.randint(1,99)
games = {}
def help():
  return """ 
    猜一个0-100之间的数字。You guessed a number from 0 - 100.
/DGuess 查看现在的状态和获取帮助。Check your current status and get help.
/DGuess number 输入number猜数字，看谁用的次数最少。Enter number and see who uses it the least often. """
def guessing(update, context):
  chatid = update.message.chat.id
  if not (chatid in games):
    games[chatid] = {'randomnumber': random.randint(1,99), "members":{}}
  print(games)
  fname = update.message.from_user.first_name
  global etries
  if len(context.args) == 0 :
    update.message.reply_text(help()) 
    return
  else:
    b = context.args[0]
    a = int(b)
    aa = b
    if fname in games[chatid]:
      games[chatid]['members'][fname] += 1
    else:
      games[chatid]['members'][fname] = 1
      msg8 = ""
      gn = "亲爱的 %s，请猜一个0-100之间的数字。\nGuess a number from 0 - 100.\n\n "%(fname)
      msg8 += gn
    if not aa.isdigit() :
      msg8 += "想什么呢审题呀 ur bad thats not a number"
    else:
      if a < 0 or a > 100:
        msg8 += "\n0-100 \nTries of %s"%(games[chatid]['members'][fname])
      else:
        if a == games[chatid]['randomnumber']:
          if etries == 0 or etries > games[chatid] : 
            etries = etries + games[chatid]
          msg8 += "Ayyy You guessed it! %s guessed it in %s tries. 天呐你竟然猜到了 概率是 '%%1' 呀！ 500 XP %s “它“值得拥有。竟然 %s 次就猜到了."%(games[chatid]['members'][fname],games[chatid],games[chatid]['members'][fname],games[chatid]) 
          games[chatid]['randomnumber'] = random.randint(1,99)
        elif a > games[chatid]['randomnumber'] :
          msg8 += "大了！重猜！It's too big! Guess again!"
        elif a < games[chatid]['randomnumber'] :
          msg8 += "小了！重猜！It's too small! Guess again!"
  msg8 += "\nTries: %s\n\nAuthorised By Noah <3\n作者：Noah"%(games[chatid]['members'])
  update.message.reply_text(msg8)

def add_handler(dp:Dispatcher):
  guess_handler = CommandHandler('DGuess',guessing)
  dp.add_handler(guess_handler)
