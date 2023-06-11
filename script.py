import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify, render_template


def get_currency(base, quote):
    url = f"https://www.google.com/finance/quote/{base}-{quote}?sa=X&ved=2ahUKEwiX1aTw-qb_AhXoQkEAHa5-BW0QmY0JegQIARAY"
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    rate = float(soup.find('div', class_='kf1m0').text)
    return rate


app = Flask(__name__, template_folder='templates/')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/<in_curr>-<out_curr>')
def api(in_curr, out_curr):
    rate = get_currency(in_curr, out_curr)
    result = {
        "Base": in_curr,
        "Quote": out_curr,
        "Rate": rate
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run()