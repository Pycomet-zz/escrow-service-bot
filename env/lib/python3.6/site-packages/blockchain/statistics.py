"""This module corresponds to functionality documented
at https://blockchain.info/api/charts_api

"""

from . import util
import json


def get(api_code=None):
    """Get network statistics.
    
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Stats` class
    """
    
    resource = 'stats?format=json'
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Stats(json_response)


def get_chart(chart_type, time_span=None, rolling_average=None, api_code=None):
    """Get chart data of a specific chart type.

    :param str chart_type: type of chart
    :param str time_span: duration of the chart.
    Default is 1 year for most charts, 1 week for mempool charts (optional)
    (Example: 5weeks)
    :param str rolling_average: duration over which the data should be averaged (optional)
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Chart` class
    """

    resource = 'charts/' + chart_type + '?format=json'
    if time_span is not None:
        resource += '&timespan=' + time_span
    if rolling_average is not None:
        resource += '&rollingAverage=' + rolling_average
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Chart(json_response)


def get_pools(time_span=None, api_code=None):
    """Get number of blocks mined by each pool.

    :param str time_span: duration of the chart.
    Default is 4days (optional)
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of dict:{str,int}
    """

    resource = 'pools'
    if time_span is not None:
        resource += '?timespan=' + time_span
    if api_code is not None:
        resource += '&api_code=' + api_code
    response = util.call_api(resource, base_url='https://api.blockchain.info/')
    json_response = json.loads(response)
    return {k: v for (k, v) in json_response.items()}


class Stats:
    def __init__(self, s):
        self.trade_volume_btc = s['trade_volume_btc']
        self.miners_revenue_usd = s['miners_revenue_usd']
        self.btc_mined = s['n_btc_mined']
        self.trade_volume_usd = s['trade_volume_usd']
        self.difficulty = s['difficulty']
        self.minutes_between_blocks = s['minutes_between_blocks']
        self.number_of_transactions = s['n_tx']
        self.hash_rate = s['hash_rate']
        self.timestamp = s['timestamp']
        self.mined_blocks = s['n_blocks_mined']
        self.blocks_size = s['blocks_size']
        self.total_fees_btc = s['total_fees_btc']
        self.total_btc_sent = s['total_btc_sent']
        self.estimated_btc_sent = s['estimated_btc_sent']
        self.total_btc = s['totalbc']
        self.total_blocks = s['n_blocks_total']
        self.next_retarget = s['nextretarget']
        self.estimated_transaction_volume_usd = s['estimated_transaction_volume_usd']
        self.miners_revenue_btc = s['miners_revenue_btc']
        self.market_price_usd = s['market_price_usd']


class Chart:
    def __init__(self, c):
        self.status = c['status']
        self.name = c['name']
        self.unit = c['unit']
        self.period = c['period']
        self.description = c['description']
        self.values = [Point(point) for point in c['values']]


class Point:
    def __init__(self, p):
        self.x = p['x']
        self.y = p['y']
