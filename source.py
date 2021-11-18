from config import *
import requests

class BitcoinApi(object):

    def __init__(self):
        self.email = MAIL
        self.password = PASS
        self.token = FORGING_BLOCK_TOKEN
        self.xpub = ""
        self.mnemonic = ""

    def create_wallet(self):
        # import pdb; pdb.set_trace()
        try:
            res1 = requests.post("https://wallet-api.forgingblock.io/v1/create-btc-mnemonic").json()
            self.mnemonic = res1['mnemonic']
            print(self.mnemonic)
            
            payload = {
                'mnemonic': self.mnemonic,
                'number': 0
            }
            res2 = requests.post("https://wallet-api.forgingblock.io/v1/retrieve-btc-wallet-address", data=payload).json()
            self.address = res2['address']
            return self.mnemonic, self.address

        except Exception as e:
            return None

    def get_xpub(self):
        payload = {
            'mnemonic': self.mnemonic,
        }
        res = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-xpub", data=payload).json()
        self.xpub = res['xpub']

        return self.xpub

    def get_wif(self):
        payload = {
            'mnemonic': self.mnemonic,
        }
        res = requests.post("https://wallet-api.forgingblock.io/v1/generate-btc-wif", data=payload).json()
        self.wif = res['wif']

        return self.wif

    def get_btc_fee(self):
        res = requests.post("https://wallet-api-demo.forgingblock.io/v1/find-btc-fee").json()
        return res['fastestFee'], res['halfHourFee'], res['hourFee']

    def get_eth_fee(self):
        res = requests.post("https://wallet-api-demo.forgingblock.io/v1/find-eth-gas").json()
        return res['FastGasPrice'], res['SafeGasPrice'], res['suggestBaseFee'] 


    def create_store(self, name):
        payload = {
            'email': self.email,
            'password': self.password,
            'xpub': self.xpub,
            'name': name
        }
        result = requests.post("https://api.forgingblock.io/create-store", data=payload).json()
        
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
            result = requests.post("https://api.forgingblock.io/connect-wallet-btc-single", data=payload).json()
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
            result = requests.post('https://api.forgingblock.io/create-invoice', data=payload).json()
            
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
            result = requests.post('https://api.forgingblock.io/check-invoice', data=payload).json()
            return result['url']

        except Exception as e:
            return "Failed"

    def check_status(self, trade):
        try:
            payload = {
                'trade': trade.trade,
                'token': trade.token,
                'invoice': trade.invoice
            }
            result = requests.post('https://api.forgingblock.io/check-invoice-status', data=payload).json()
            print(result)
            return result['status']

        except Exception as e:
            return "Failed"


    def get_btc_balance(address:str) -> object:
        try:
            payload = {
                'address': address
            }
            result = requests.post('https://wallet-api.forgingblock.io/v1/find-btc-address-balance', data=payload).json()
            return result

        except Exception as e:
            return "Failed"

    def get_eth_balance(address:str) -> object:
        try:
            payload = {
                'address': address
            }
            result = requests.post('https://wallet-api.forgingblock.io/v1/find-eth-address-balance', data=payload).json()
            return result

        except Exception as e:
            return "Failed"