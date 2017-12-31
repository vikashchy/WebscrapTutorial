from urllib.request import urlopen
from bs4 import BeautifulSoup
website = 'http://timesofindia.indiatimes.com/business/india-business/india-should-focus-more-on-reducing-poverty-than-inequality-niti-aayog/articleshow/60260320.cms'
html=urlopen(website)
bsObj = BeautifulSoup(html,"html.parser")
print(bsObj.title.text)
nameList = bsObj.findAll('div', attrs={'class': 'Normal'})
for nameList_ in nameList:
    pass
    # print(nameList_.text)
urlList = bsObj.findAll('a')
# for _urllist in urlList:
#     try:
#         nextUrl = _urllist['href']
#         title = _urllist['title']
#     except:
#         continue
#         # nextUrl = 'NA'
#         # title = 'NA'
#     print(nextUrl+'------>' +title)
nav = bsObj.find('nav',class_='Normal')
print(nav)
