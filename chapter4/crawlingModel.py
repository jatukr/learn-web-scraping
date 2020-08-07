import requests
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, topic, title, body, url):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
        Flexible printing function controls output
        """
        print('New article found for topic : {}'.format(self.topic))
        print('Title : {}'.format(self.title))
        print('Body : {}'.format(self.body))
        print('URL : {}'.format(self.url))


class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty
        string if no object is found for the given selector
        """
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ""

        """
        selectedELems = pageObj.select(selector)
        if selectedELems is not None and len(selectedELems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedELems])
        """

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            # Check to see whether it's a relative or an absolute URL
            if site.absoluteUrl:
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL. Skipping!')
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()


"""
    def parse(self, site, url):
        
        #  Extract content from a given page URL
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

"""
"""
def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')
"""
"""
def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find_all('p', {'class': 'css-158dogj'})
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)
"""
"""
def scrapeBooking(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'post-body'}).text
    return Content(url, title, body)

"""
"""url = 'https://www.brookings.edu/blog/future-development'\
      '/2018/01/26/delivering-inclusive-urban-access-3-unc'\
      'omfortable-truths/'
content = scrapeBooking(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)"""

crawler = Crawler()
"""
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1',
     'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'h1', 'div.post-body'],
    ['New York Times', 'http://nytimes.com',
     'h1', 'p.story-content']
]
"""
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'https://ssearch.oreilly.com/?q=', 'article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content', 'h3.search-result-title a',
     False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
]

sites = []
websites = []

for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3],
                         row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print('Getting info about : ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)

"""
crawler.parse(websites[0], 'http://shop.oreilly.com/product/'
                           '0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/'
                           'us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/'
                           'techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/'
                           '28/business/energy-environment/oil-boom.html')
"""