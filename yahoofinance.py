import sys
import PyQt4
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import os
import time
path = "D:/YahooFiancer"


# class Client(QWebPage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()
#
#     def on_page_load(self):
#         self.app.quit()


# client_response = Client(url)
# source = client_response.mainFrame().toHtml()
# soup = bs.BeautifulSoup(source, 'lxml')
# js_test = soup.find('p', class_='jstest')
# print(js_test.text)

def Check_Yahoo():
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:25]:
        try:
            e = e.replace("D:/Yahoo/intraQuarter/intraQuarter/_KeyStats\\","")
            link = "http://finance.yahoo.com/q/ks?s=" + e.upper() + "+Key+Statistics"
            resp = urllib.request.urlopen(link).read().decode("utf-8")
            # client_response = Client(link)
            # source = client_response.mainFrame().toHtml()
            # source = resp.
            soup = bs.BeautifulSoup(resp, 'lxml')
            print(soup)
            # save = "forward/" + str(e) + ".html"
            # store = open(save, "w")
            # store.write(str(source))

            # time.sleep(5)
            # store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)


Check_Yahoo()