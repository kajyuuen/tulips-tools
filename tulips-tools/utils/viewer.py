import os
from tulips import Tulips

class Viewer:
    def __init__(self, name, password):
        self.tulips = Tulips(name, password)
        self.tulips.login()

    def borrow(self):
        info = self.tulips.borrow()
        if len(info) == 0:
            print("現在借りている本はありません。")
            return
        for i in info:
            print("- 「{}」: {}".format(i["title"], i["返却予定"]))

    def history(self):
        info = self.tulips.history()
        if len(info) == 0:
            print("今まで借りた本は無いようです。")
            return
        for i in info:
            print("- 「{}」: {}".format(i["title"], i["貸出日"]))
