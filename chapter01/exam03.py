from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.hrd.go.kr/hrdp/co/pcobo/PCOBO0100P.do?tracseId=AIG20170000168332&tracseTme=2&trainstCstmrId=undefined#undefined")
if title == None:
    print("Title could not be found")
else:
    print(title)

