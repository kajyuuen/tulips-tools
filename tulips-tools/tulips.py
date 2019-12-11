import os
from mechanize import Browser
from bs4 import BeautifulSoup

class Tulips:
    def __init__(self, user, passwd):
        self.url = "https://www.tulips.tsukuba.ac.jp/opac/user/top"
        self.user = user
        self.passwd = passwd
        self.browser = Browser()
        self.is_login = False

    def login(self):
        # Login
        self.browser.open(self.url)
        self.browser.select_form(nr=0)

        self.browser["j_username"] = self.user
        self.browser["j_password"] = self.passwd
        self.browser.submit()

        # Re submit
        self.browser.open(self.url)

        self.browser.response().read()
        self.browser.select_form(nr=0)
        self.browser.submit()
        self.is_login = True

    def borrow(self):
        self.__is_login()
        url = "https://www.tulips.tsukuba.ac.jp/opac/user/holding-borrowings"

        self.browser.open(url)
        html = self.browser.response().read()
        result = self.__extract_book_info(html)
        return result

    def history(self):
        self.__is_login()
        url = "https://www.tulips.tsukuba.ac.jp/opac/user/loan-history"

        self.browser.open(url)
        html = self.browser.response().read()
        history = self.__extract_book_info(html)
        return history

    def __is_login(self):
        if not self.is_login:
            raise Exception("Please login")

    def __extract_book_info(self, html):
        book_infos = []
        for book in BeautifulSoup(html, features="html5lib").select(".searchCard"):
            book_info = {}
            book_info["title"] = book.find("h3").getText()
            key, value = None, None
            for i in book.find_all(['dt', 'dd']):
                if i.name == "dt":
                    key = i.getText()
                elif i.name == "dd":
                    value = i.getText()
                if key is not None and value is not None:
                    book_info[key] = value
                    key, value = None, None
            book_infos.append(book_info)
        return book_infos

if __name__ == "__main__":
    tulips = Tulips(os.environ["LIB_USER"], os.environ["LIB_PASSWD"])
    tulips.login()
    tulips.history()
    tulips.borrow()
