import os
from tulips import Tulips
from utils.config import load_config
from slackbot.bot import respond_to

@respond_to('\S*返却日\S*')
def borrow(message):
    name, password = load_config()
    tulips = Tulips(name, password)
    tulips.login()

    info = tulips.borrow()
    if len(info) == 0:
        message.reply("YUKI.N> 今、借りている本は無い。")
        return
    
    text = ""
    for i in info:
        text += "YUKI.N>「{}」を{}までに\n".format(i["title"], i["返却予定"])
    message.reply(text + "YUKI.N> 返却して。")
