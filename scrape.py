import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

SITES = {
    "eldeber": "https://eldeber.com.bo/",
    "lostiempos": "https://www.lostiempos.com/",
    "larazon": "https://www.la-razon.com/"
}

def scrape_site(name, url):
    headers = {"User-Agent": "NewsAggregatorBot/1.0 (+https://github.com/tu-usuario)"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    articles = []
    for item in soup.select("h2 a")[:5]:
        title = item.get_text(strip=True)
        link = item.get("href")
        if link and not link.startswith("http"):
            link = url.rstrip("/") + "/" + link.lstrip("/")
        articles.append({"source": name, "title": title, "url": link})
    time.sleep(2)
    return articles

def main():
    allnews = []
    for name, url in SITES.items():
        try:
            print(f"Scraping {name} …")
            allnews += scrape_site(name, url)
        except Exception as e:
            print(f"Error scraping {name}: {e}")
    data = {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "articles": allnews
    }
    with open("data/news.json", "w", encoding="utf‑8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Scraping completo.")

if __name__ == "__main__":
    main()
