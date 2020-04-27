"""This module allows users to push hex encoded transactions to the bitcoin network.
Corresponds to https://blockchain.info/pushtx
"""

from . import util


def pushtx(tx, api_code=None):
    """Push a hex encoded transaction to the network.
    
    :param str tx: hex encoded transaction
    :param str api_code: Blockchain.info API code (optional)
    """
    params = {'tx': tx}
    if api_code is not None:
        params['api_code'] = api_code
    util.call_api('pushtx', params)
