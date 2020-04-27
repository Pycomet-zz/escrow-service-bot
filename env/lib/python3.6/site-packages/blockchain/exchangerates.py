"""This module corresponds to functionality documented at 
https://blockchain.info/api/exchange_rates_api
"""

import json
from . import util


def get_ticker(api_code=None):
    """Call the 'ticker' method and return a dictionary
    of :class:`Currency` objects.
    
    :param str api_code: Blockchain.info API code (optional)
    :return: a dictionary in the format of ccy_symbol(str):currency(:class:`Currency`)
    """
    
    response = util.call_api('ticker' if api_code is None else 'ticker?api_code=' + api_code)
    json_response = json.loads(response)
    ticker = {}
    for key in json_response:
        json_ccy = json_response[key]
        ccy = Currency(json_ccy['last'],
                       json_ccy['buy'],
                       json_ccy['sell'],
                       json_ccy['symbol'],
                       json_ccy['15m'])
        ticker[key] = ccy
    return ticker


def to_btc(ccy, value, api_code=None):
    """Call the 'tobtc' method and convert x value in the provided currency to BTC.
    
    :param str ccy: currency code
    :param float value: value to convert
    :param str api_code: Blockchain.info API code
    :return: the value in BTC
    """
    
    res = 'tobtc?currency={0}&value={1}'.format(ccy, value)
    if api_code is not None:
        res += '&api_code=' + api_code
    return float(util.call_api(res))


def to_fiat(ccy, value, api_code=None):
    """Call the 'frombtc' method and convert x value in the provided currency to BTC.

    :param str ccy: currency code
    :param float value: BTC value to convert
    :param str api_code: Blockchain.info API code
    :return: the value in fiat currency
    """

    res = 'frombtc?currency={0}&value={1}'.format(ccy, value*100000000)
    if api_code is not None:
        res += '&api_code=' + api_code
    return float(util.call_api(res))


class Currency:
    def __init__(self, last, buy, sell, symbol, p15min):
        self.last = last
        self.buy = buy
        self.sell = sell
        self.symbol = symbol
        self.p15min = p15min
