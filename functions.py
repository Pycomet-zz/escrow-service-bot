from config import *
from model import Trade, Dispute, session

import random
import string
from datetime import datetime
import cryptocompare

client = Client(API_KEY, API_SECRET)
accounts = client.get_accounts()

eth_account = accounts.data[4]
btc_account = accounts.data[5]

def get_coin_price(coin_code, currency_code):
    """
    Returning the current btc/eth price for specified currency
    """
    data = cryptocompare.get_price(coin_code, currency_code)
    return data[coin_code][currency_code]


def generate_id():
    "Return unique id"
    u_id = ""
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits

    option = lower_case + upper_case + digits

    for i in range(10):
        u_id += str(random.choice(option))

    return u_id

def get_trade(id):
    "Return the trade"
    try:
        trade = session.query(Trade).filter(Trade.id == id).one()
        return trade

    except:
        return "Not Found"

def get_recent_trade(user):
    """
    Return a trade matching a seller
    """
    trade = session.query(Trade).filter(Trade.seller == user.id)
    if trade != None:
        return trade[-1]
    
    else:
        trade = session.query(Trade).filter(Trade.buyer == user.id)
        return trade[-1]


def open_new_trade(user, currency):
    """
    Returns a new trade
    """
    trade = Trade(
        id =  generate_id(),
        seller = user.id,
        currency = currency,
        payment_status = False,
        created_at = str(datetime.now()),
        is_open = True,
        )

    session.add(trade)
    session.commit()


def add_coin(user, coin):
    """
    Update trade instance with coin preference
    """
    trade = get_recent_trade(user)
    trade.coin = str(coin)

    if coin == "BTC":
        trade.receive_address_id = btc_account.create_address().address
    elif coin == "ETH":
        trade.receive_address_id = eth_account.create_address().address
    else:
        pass

    session.add(trade)

def add_price(user, price):
    """
    Update trade instance with price of service
    """
    trade = get_recent_trade(user)
    trade.price = float(price)
    session.add(trade)

def add_wallet(user, address):
    """
    Update trade instance with wallet for seller
    """
    trade = get_recent_trade(user)
    trade.wallet = str(address)
    session.add(trade)
    session.commit()

def add_buyer(trade, buyer):
    "Add Buyer To Trade"
    trade.buyer = buyer.id
    session.add(trade)
    session.commit()

def get_receive_address(trade):
    "Return the receive address"

    if trade.coin == "BTC":
        wallet = btc_account.get_address(trade.receive_address_id).address
    
    elif trade.coin == "ETH":
        wallet = eth_account.get_address(trade.receive_address_id).address

    else:
        return "ERROR!"

    return wallet

def delete_trade(trade_id):
    "Delete Trade"
    trade = session.query(Trade).filter(Trade.id == trade_id).delete()
    
    if trade == None:
        return "Not Found!"
    else:
        session.commit()
        return "Complete!"


def check_trade(user, trade_id):
    "Return trade info"

    trade = session.query(Trade).filter(Trade.id == trade_id).first()
    if trade == None:

        return "Not Found"

    else:
        add_buyer(
            trade=trade,
            buyer=user
        )
        return trade


def get_trades(user):
    "Retrun list of trades the user is in"
    
    sells = session.query(Trade).filter(Trade.seller == user.id).all()
    buys = session.query(Trade).filter(Trade.buyer == user.id).all()

    return sells, buys

def confirm_pay(trade):
    "Confirm Payment"
    trade.payment_status = True
    session.add(trade)
    session.commit()

def check_payment(trade, hash):
    "Returns Status Of Payment"

    try:
        tx = blockexplorer.get_tx(hash)

        #Check if it is the same
        if trade.coin == "BTC":
            transaction_hash = btc_account.get_address_transactions(trade.receive_address_id).data[-1].network.hash
        else:
            transaction_hash = eth_account.get_address_transactions(trade.receive_address_id).data[-1].network.hash

        if transaction_hash == tx.hash:
            confirm_pay(trade)
            return "Approved"

    except:
        return "Pending"

def pay_funds_to_seller(trade):
    "Calculate Fees And Send Funds To Seller"
    coin_price = get_coin_price(
        coin_code=trade.coin,
        currency_code=trade.currency
    )

    value = float(trade.price)/float(coin_price)

    service_charge = 0.01 * float(value)
    fees = 0.0149 * value

    pay_price = float(value) - service_charge + fees

    price = "%.4f" % pay_price

    if trade.coin == "BTC":
        btc_account.send_money(
            to = trade.wallet,
            amount = str(price),
            currency = "BTC"
        )
        close_trade(trade)

    elif trade.coion == "ETH":
        eth_account.send_money(
            to = trade.wallet,
            amount = str(price),
            currency = "ETH",
        )
        close_trade(trade)

    else:
        pass


def close_trade(trade):
    "Closing The Trade"
    trade.is_open = False
    session.add(trade)
    session.commit()




def pay_to_buyer(trade, wallet):
    "Send Funds To Buyer"

    coin_price = get_coin_price(
        coin_code=trade.coin,
        currency_code=trade.currency
    )

    value = float(trade.price)/float(coin_price)

    service_charge = 0.01 * float(value)
    fees = 0.0149 * value

    pay_price = float(value) - service_charge + fees

    price = "%.4f" % pay_price

    if trade.coin == "BTC":
        btc_account.send_money(
            to = wallet,
            amount = str(price),
            currency = "BTC"
        )
        close_trade(trade)

    elif trade.coion == "ETH":
        eth_account.send_money(
            to = trade.wallet,
            amount = str(price),
            currency = "ETH",
        )
        close_trade(trade)

    else:
        pass



#######################DISPUTE############################
def create_dispute(user, trade):
    "Returns a newly created disput to a trade"

    dispute = Dispute(
        id = generate_id(),
        user = user.id,
        info = trade,
    )
    trade.dispute = True

    if user.id == trade.seller and user.id == trade.buyer:
        dispute.is_buyer = True
        dispute.is_seller = True

    elif user.id != trade.seller and user.id == trade.buyer:
        dispute.is_buyer = True
        dispute.is_seller = False       

    elif user.id == trade.seller and user.id != trade.buyer:
        dispute.is_buyer = False
        dispute.is_seller = True

    else:
        dispute.is_seller = False
        dispute.is_buyer = False

    session.add(dispute)
    session.add(trade)
    session.commit()

    return dispute