from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html.read(), 'html.parser')
nameList = soup.find_all(id='text')

for name in nameList:
    print(name.get_text())