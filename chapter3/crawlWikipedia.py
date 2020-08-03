from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
r = requests.get('http://id.wikipedia.org', a)

pages = set()
def getLinks(articleUrl):
    global pages
    try:
        html = urlopen(f'http://id.wikipedia.org{articleUrl}')
        bs = BeautifulSoup(html, 'html.parser')
    except HTTPError as e:
        return None
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find('div',{'id': 'right-navigation'}).nav.div.ul.li.next_sibling)
        #print(bs.find(id='ca-edit').find('a').attrs['href'])
    except AttributeError as e:
        print('This page is missing something! continuing.')

    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPages = link.attrs['href']
                #print('-'*20)
                #print(newPages)
                pages.add(newPages)
                #getLinks(newPages)

getLinks('/wiki/Partai_Demokrasi_Indonesia_Perjuangan')