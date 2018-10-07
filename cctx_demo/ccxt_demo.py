import asyncio
import json
import time

import ccxt


def run():
    market = ccxt.hitbtc2()
    while True:
        market.rateLimit = 200
        print('fetching tickers...')
        print('tickers: {}'.format(market.fetch_tickers()))


def get_coinmarketcap_currencies():
    currencies = ccxt.coinmarketcap().fetch_currencies()
    file = open('data.json', 'w', encoding='utf-8')
    line = json.dumps(dict(currencies), ensure_ascii=False) + "\n"
    file.write(line)


def fetch_tickers():
    retries = 0
    while retries < 3:
        retries += 1
        print('retries: {}'.format(retries))
        try:
            a = 1 / 0
            print('1'.format(a))
            return a
        except TimeoutError as e:
            print('e: {}'.format(e))
            # continue


if __name__ == "__main__":
    print(fetch_tickers())
