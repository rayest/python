import multiprocessing
from datetime import datetime
from urllib import request

import time

import ccxt
import requests
from bs4 import BeautifulSoup


def get_history(coin):
    url = 'https://coinmarketcap.com/currencies/' + coin + '/historical-data?start=20130428&end=20180503'
    response = request.Request(url)
    page = request.urlopen(response).read()
    bsObj = BeautifulSoup(page, 'html.parser')
    trs = bsObj.tbody.find_all('tr', {'class': 'text-right'})
    for tr in trs:
        tds = tr.find_all('td')
        date = tds[0].get_text()
        Open = tds[1]['data-format-value']
        High = tds[2]['data-format-value']
        Low = tds[3]['data-format-value']
        Close = tds[4]['data-format-value']
        Volume = tds[5]['data-format-value']
        marketCap = tds[6]['data-format-value']
    print(coin)
    # save()


def parse_history():
    coins = parse_coins()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for coin in coins:
        pool.apply_async(get_history, (coin,))
    pool.close()
    pool.join()


def parse_coins():
    #  获取所有货币
    url = 'https://coinmarketcap.com/all/views/all/'
    response = request.Request(url)
    page = request.urlopen(response).read()
    bsObj = BeautifulSoup(page, 'html.parser')
    spans = bsObj.tbody.find_all('span', {'class': 'currency-symbol'})
    coins = []
    for span in spans:
        coin = span.find_all('a')[0]['href'].split('/')[2]
        coins.append(coin)
    return coins


def a():
    response = request.Request(
        'https://coinmarketcap.com/currencies/farstcoin/historical-data/?start=20130428&end=20180504')


def b():
    response = requests.get('https://api.coinmarketcap.com/v2/ticker')
    data = response.json().get('data')
    items = data.items()
    for key, value in items:
        print(key)
        print(value)
        break


from multiprocessing import Pool


def c():
    coinmarket = ccxt.coinmarketcap()
    return coinmarket.fetch_ticker('BTC/USD')


def output_utc():
    return datetime.utcnow()


if __name__ == '__main__':
    print(b())
