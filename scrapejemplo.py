# scraper_larazon.py
import requests
from bs4 import BeautifulSoup

def scrape_la_razon(limit=5):
    url = 'https://www.la-razon.com'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, 'html.parser')
    results = []

    for article in soup.select('article')[:limit]:
        title_tag = article.find('h2')
        link_tag = article.find('a')
        img_tag = article.find('img')

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag['href']
        if not link.startswith('http'):
            link = url + link
        image = img_tag['src'] if img_tag else ''
        summary = article.get_text(strip=True)[:200]

        results.append({
            'title': title,
            'link': link,
            'image': image,
            'summary': summary
        })

    return results
