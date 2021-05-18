import requests
from bs4 import BeautifulSoup
import random

response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.content)

allLinks = soup.find(id="bodyContent").find_all("a")
random.shuffle(allLinks)
linkToScrape = 0

for link in allLinks:
	if link['href'].find("/wiki/") == -1:  #other wiki articles
		continue
    
	linkToScrape = link
	break

print(linkToScrape)
