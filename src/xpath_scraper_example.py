# Tutorial: 'https://3583bytesready.net/2016/08/17/scraping-data-python-xpath/'
# run: 'python xpath_scraper_example.py'

# In OSX install with: 'sudo easy_install -U requests'
import requests
# In OSX install with: 'sudo easy_install -U lxml'
from lxml import html

pageContent=requests.get(
     'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo'
)

tree = html.fromstring(pageContent.content)

# To see the page html uncomment the following line
# print pageContent.content

# Do not use browser tags such as 'tbody'
goldWinners = tree.xpath('//*[@id="mw-content-text"]/div/table/tr/td[2]/a[1]/text()')
silverWinners = tree.xpath('//*[@id="mw-content-text"]/div/table/tr/td[3]/a[1]/text()')
# bronzeWinner we need rows where there's no rowspan
bronzeWinners = tree.xpath('//*[@id="mw-content-text"]/div/table/tr/td[not(@rowspan=2)]/a[1]/text()')

medalWinners=goldWinners+silverWinners+bronzeWinners

# Count number of medals of each winner
medalTotals={}
for name in medalWinners:
    if medalTotals.has_key(name):
        medalTotals[name]=medalTotals[name]+1
    else:
        medalTotals[name]=1

print "List of Olympic medalists in judo:"

# Print winner sorted from largest number of medals to smallest
for result in sorted(medalTotals.items(), key=lambda x:x[1],reverse=True):
      print '%s: %s' % result
