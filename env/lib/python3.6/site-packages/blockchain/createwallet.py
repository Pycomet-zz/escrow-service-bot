"""This module corresponds to functionality documented
at https://blockchain.info/api/create_wallet

"""

from . import util
import json


def create_wallet(password, api_code, service_url, priv=None, label=None, email=None):
        """Create a new Blockchain.info wallet. It can be created containing a 
        pre-generated private key or will otherwise generate a new private key. 

        :param str password: password for the new wallet. At least 10 characters.
        :param str api_code: API code with create wallets permission
        :param str service_url: URL to an instance of service-my-wallet-v3 (with trailing slash)
        :param str priv: private key to add to the wallet (optional)
        :param str label: label for the first address in the wallet (optional)
        :param str email: email to associate with the new wallet (optional)
        :return: an instance of :class:`WalletResponse` class
        """
        
        params = {'password': password, 'api_code': api_code}
        if priv is not None:
            params['priv'] = priv
        if label is not None:
            params['label'] = label
        if email is not None:
            params['email'] = email
        
        response = util.call_api("api/v2/create", params, base_url=service_url)
        json_response = json.loads(response)
        return CreateWalletResponse(json_response['guid'],
                                    json_response['address'],
                                    json_response['label'])


class CreateWalletResponse:
    
    def __init__(self, identifier, address, label):
        self.identifier = identifier
        self.address = address
        self.label = label
