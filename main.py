# Import Packages
import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream'
urls = 'https://detik.com'

ourUrl = urllib.request.urlopen(url)

# Create a BeautifulSoup object, which represents the document as a nested data structure
# Parse the page
soup = BeautifulSoup(ourUrl, 'html.parser')
print(soup.prettify())
print(soup.find_all('div', {'class': 'lemon--div__373c0__1mboc margin-b2__373c0__abANL border-color--default__373c0__3-ifU'}) )