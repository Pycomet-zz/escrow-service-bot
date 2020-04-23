from config import *
from model import Trade, session

import random
import string
from datetime import datetime

client = Client(API_KEY, API_SECRET)
accounts = client.get_accounts()

eth_account = accounts.data[3]
btc_account = accounts.data[4]

def get_price(coin_code, currency_code):
    """
    Returning the current btc/eth price for specified currency
    """
    data = cryptocompare.get_price(coin=coin_code, curr=currency_code)
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


def get_recent_trade(user):
    """
    Return a trade matching a seller
    """
    try:
        trade = session.query(Trade).filter(Trade.seller == user.id)[-1]
        return trade
    except:
        trade = session.query(Trade).filter(Trade.buyer == user.id)[-1]
        return trade
    finally:
        return "Not Found"


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
        )

    session.add(trade)
    session.commit()


def add_coin(user, coin):
    """
    Update trade instance with coin preference
    """
    trade = get_recent_trade(user)
    trade.coin = coin
    session.add(trade)

def add_price(user, price):
    """
    Update trade instance with price of service
    """
    trade = get_recent_trade(user)
    trade.price = price
    session.add(trade)

def add_wallet(user, address):
    """
    Update trade instance with wallet for seller
    """
    trade = get_recent_trade(user)
    trade.wallet = address
    session.add(trade) 


def send_trade_info(user):
    """
    Send Out Trade Information To User
    """
    trade = get_recent_trade(user)

    bot.send_message(
        user.id,
        emoji.emojize(
            f"""
    Trade Details
    -----------------

    ID --> <b>{trade.id}</b>
    Price --> <b>{trade.price} {trade.currency}</b>
    Preferred method of payment --> <b>{trade.coin}</b>
    Created on --> <b>{trade.created_at}</b>

    Share only the trade ID with your customer to allow his/her join the trade. They would receive all the related information when they join.
            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )


def delete_trade(trade_id):
    "Delete Trade"
    trade = session.query(Trade).filter(Trade.id == trade_id).delete()
    
    if trade == None:
        return "Not Found!"
    else:
        session.commit()
        return "Complete!"
