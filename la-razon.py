import requests
from bs4 import BeautifulSoup
import time

def scrape_la_razon(section_url, max_items=10):
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(section_url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    articles = []
    for tag in soup.select('article h2 a')[:max_items]:
        title = tag.get_text(strip=True)
        link = tag['href']
        if link.startswith('/'):
            link = 'https://www.la-razon.com' + link
        articles.append({'title': title, 'link': link})
    return articles

if __name__ == '__main__':
    url = 'https://www.la-razon.com/politico/'
    for a in scrape_la_razon(url):
        print(a['title'], a['link'])
        time.sleep(1)
