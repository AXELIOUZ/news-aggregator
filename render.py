from jinja2 import Environment, FileSystemLoader
import json
from datetime import datetime

def render():
    data = json.load(open("data/news.json", encoding="utf‑8"))
    env = Environment(loader=FileSystemLoader("templates"))
    tmpl = env.get_template("base.html")
    html = tmpl.render(news=data["articles"], fetched=data["fetched_at"])
    with open("index.html", "w", encoding="utf‑8") as f:
        f.write(html)
    print("HTML generado.")

if __name__ == "__main__":
    render()
