from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.hrd.go.kr/hrdp/co/pcobo/PCOBO0100P.do?tracseId=AIG20170000168332&tracseTme=2&trainstCstmrId=undefined#undefined")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.html.body.div.form.input)
