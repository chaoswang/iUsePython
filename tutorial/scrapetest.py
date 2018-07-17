from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.title
    except AttributeError as e:
        print(e)
        return None
    return title

title = getTitle("http://ny.310v.com:3389/dt/index.html?mid=11262861&tp=match_fx")
if title != None:
    print(title)
