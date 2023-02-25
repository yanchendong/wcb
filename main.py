#encoding=utf-8
from wxpy import *
from ct import res
 
bot = Bot(cache_path=True)
name = input("针对谁？")
myfriend = bot.friends().search(u"{}".format(name))[0]
@bot.register(myfriend, TEXT)
def print_msg1(msg1):
    msg = str(msg1)[len(name) + 3:-7]
    if msg.find("bot ") == 0:
        msg = msg.replace("bot ","")
        print(msg)
        myfriend.send("[bot]" + res(msg))

bot.join()