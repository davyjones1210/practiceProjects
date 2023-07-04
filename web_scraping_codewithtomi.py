import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content,'lxml')
title = soup.find_all('h2', {'class':'post-title'})

with open('web_scraper_codewithtomi.txt', 'a') as f:
    for t in title:
        f.write(t.getText().strip() + "\n")

