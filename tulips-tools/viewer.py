import os
from tulips import Tulips

class Viewer:
    def __init__(self, name, password):
        self.tulips = Tulips(name, password)
        self.tulips.login()

    def history(self):
        info = self.tulips.history()
        for i in info:
            print("- 「{}」: {}".format(i["title"], i["貸出日"]))

    def borrow(self):
        info = self.tulips.borrow()
        for i in info:
            print("- 「{}」: {}".format(i["title"], i["返却予定"]))
