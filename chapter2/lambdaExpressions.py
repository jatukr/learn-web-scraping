from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
#tags = bs.find_all(lambda tag: len(tag.attrs) == 2)
teks = bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
teksL = bs.find_all('', text='Or maybe he\'s only resting?')
