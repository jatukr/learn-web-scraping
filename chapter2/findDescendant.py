from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html.read(), 'html.parser')

print('Find Children')
for child in soup.find('table', {'id': 'giftList'}).children:
    print(child)

print('\nFind Descendant')
for child in soup.find('table', {'id': 'giftList'}).descendants:
    print(child)