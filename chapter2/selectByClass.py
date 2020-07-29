from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html.read(), 'html.parser')
nameList =soup.find_all('span', {'class': 'green'})
#findHeader = soup.find_all(['h1','h2','h3','h4','h5','h6'])

for name in nameList:
    print(name)