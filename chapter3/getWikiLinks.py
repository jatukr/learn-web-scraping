from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    global pages
    try:
        html = urlopen(f'http://en.wikipedia.org{articleUrl}')
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id': 'bodyContent'}).find_all(
            'a', href=re.compile('^(/wiki/)((?!:).)*$'))
    except AttributeError as e:
        return None


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
