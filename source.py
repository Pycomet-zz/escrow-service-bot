from config import *
import requests

class BitcoinApi(object):

    def __init__(self):
        email = MAIL
        password = PASS
        token = FORGING_BLOCK_TOKEN
        xpub = ""
        mnemonic = ""

    def create_wallet(self):
        # import pdb; pdb.set_trace()
        try:
            res1 = requests.post("https://wallet-api.forgingblock.io/v1/create-btc-mnemonic")
            self.mnemonic = res1['mnemonic']

            payload = {
                'mnemonic': self.mnemonic,
                'number': 0
            }
            res2 = requests.post("https://wallet-api.forgingblock.io/v1/retrieve-btc-wallet-address", params=payload)
            self.address = res2['address']
            return self.mnemonic, self.address

        except Exception as e:
            return None

    def get_xpub(self):
        payload = {
            'mnemonic': self.mnemonic,
        }
        res = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-xpub", params=payload)
        self.xpub = res['xpub']

        return self.xpub


    def create_store(self, name):
        payload = {
            'email': self.email,
            'password': self.password,
            'xpub': self.xpub,
            'name': name
        }
        result = requests.post("https://api.forgingblock.io/create-store", params=payload)
        
        self.trade = result['trade']
        self.token = result['token']
        self.store = result['store']
        return self.trade, self.token, self.store

    
    def connect_store(self):
        try:
            payload = {
                'email': self.email,
                'password': self.password,
                'address': self.address,
                'store': self.store
            }
            result = requests.post("https://api.forgingblock.io/connect-wallet-btc-single", params=payload)
            return result['success']

        except Exception as e:
            return "Failed"


    
    def create_invoice(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'amount': trade.price,
                'currency': trade.currency,
            }
            result = requests.post('https://api.forgingblock.io/create-invoice', params=payload)
            
            self.invoice = result['id']
            return self.invoice

        except Exception as e:
            return "Failed"

    def get_payment_url(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'invoice': trade.invoice
            }
            result = requests.post('https://api.forgingblock.io/check-invoice', params=payload)
            return result['payUrl']

        except Exception as e:
            return "Failed"

    def check_status(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'invoice': trade.invoice
            }
            result = requests.post('https://api.forgingblock.io/check-invoice-status', params=payload)
            return result['status']

        except Exception as e:
            return "Failed"