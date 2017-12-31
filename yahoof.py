from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen
import time

def importTicker():
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    return df[0][0][1:]

def fetchWebpage():
    for tick in importTicker():
        try:
            url = "https://in.finance.yahoo.com/quote/" + tick + "/key-statistics?p=" + tick
            page = requests.get(url)
            print(url)
            filename = "D:/yahoofinance/" + tick + ".html"
            f = open(filename, 'w')
            f.write(str(page.content))
            f.close()
        except:
            print("Exception Occured for {}".format(tick))

def viewCurrent():
    for tick in importTicker():
        url = "https://in.finance.yahoo.com/quote/"+tick+"/?p="+tick
        html = urlopen(url)
        bs4Obj = BeautifulSoup(html,"lxml")
        stk = bs4Obj.find("div", { "class" : "D(ib) Fw(200) Mend(20px)" })
        print(tick + "--->" + stk.text)
        # time.sleep(1)

if __name__ == "__main__":
    # viewCurrent()
    fetchWebpage()