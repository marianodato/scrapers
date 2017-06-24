import requests
from lxml import html

pageContent=requests.get(
     'https://en.wikipedia.org/wiki/List_of_Arsenal_F.C._players'
)

tree = html.fromstring(pageContent.content)

players = tree.xpath('//*[@id="mw-content-text"]/div/table/tr/th/span/span/a/text()')

appearances = tree.xpath('//*[@id="mw-content-text"]/div/table/tr/td[6]/text()')

playerAppearances={}
for i in range(0,len(players)):
        playerAppearances[i] = appearances[i]

print "List of Arsenal F.C. players with 100 or more appearances:"

for result in sorted(playerAppearances.items(), key=lambda x:x[1],reverse=True):
      print players[result[0]] + ": " + result[1]
