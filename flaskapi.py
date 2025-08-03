# app.py
from flask import Flask, jsonify
from scraper_larazon import scrape_la_razon

app = Flask(__name__)

@app.route('/api/news')
def news():
    data = scrape_la_razon()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
