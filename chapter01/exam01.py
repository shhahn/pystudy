from urllib.request import urlopen
#Retrieve HTML string from the URL
html = urlopen("http://www.hrd.go.kr/hrdp/co/pcobo/PCOBO0100P.do?tracseId=AIG20170000168332&tracseTme=2&trainstCstmrId=undefined#undefined")
print(html.read())