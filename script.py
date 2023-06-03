import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify


def get_currency(base, quote):
    url = f"https://www.google.com/finance/quote/{base}-{quote}?sa=X&ved=2ahUKEwiX1aTw-qb_AhXoQkEAHa5-BW0QmY0JegQIARAY"
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    rate = float(soup.find('div', class_='kf1m0').text)
    return rate


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>CurrencyXchange-API</h1> <p>Example URL: /api/v1/usd-eur'


@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr, out_curr):
    rate = get_currency(in_curr, out_curr)
    result = {
        "Base": in_curr,
        "Quote": out_curr,
        "Rate": rate
    }
    return jsonify(result)
app.run()