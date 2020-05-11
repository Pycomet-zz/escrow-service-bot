from config import *
from keyboard import *
from functions import *


def start_seller(user):
    """
    This is the handler to start seller options
    """
    keyboard = seller_menu()

    bot.send_message(
        user.id,
        emoji.emojize(
            ":smile: What would you like to do today?",
            use_aliases=True
        ),
        reply_markup=keyboard
    )


def start_buyer(user):
    """
    This is the handler to start buyer options
    """
    keyboard = buyer_menu()

    bot.send_message(
        user.id,
        emoji.emojize(
            ":smile: What would you like to do today?",
            use_aliases=True
        ),
        reply_markup=keyboard
    )

######################SELLER GRID#####################

def select_coin(user):
    """
    Selecting the right coin option for trade
    """
    keyboard = coin_menu()

    bot.send_message(
        user.id,
        emoji.emojize(
            ":money_bag: What is your preferred coin for payment ? ",
            use_aliases=True
        ),
        reply_markup=keyboard
    )


def trade_price(user):
    """
    Receive user input on trade price
    """
    question = bot.send_message(
        user.id,
        emoji.emojize(
            ":money_bag: How much are you expecting to be paid in your local currency? ",
            use_aliases=True
        )
    )
    
    bot.register_next_step_handler(question, trade_address)

def trade_address(msg):
    """
    Recieve user input on trade wallet address
    """
    price = msg.text

    add_price(
        user=msg.from_user,
        price=float(price)
        )

    #REQUEST WALLET ADDRESS
    question = bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            ":money_bag: Paste the wallet address to which you will recieve payment (Confirm the wallet address to make sure it is correct) ",
            use_aliases=True
        )
    )
    bot.register_next_step_handler(question, process_trade)



def process_trade(msg):
    """
    Assigning of trade wallet
    """
    wallet = msg.text

    add_wallet(
        user=msg.from_user,
        address=wallet
    )

    trade = get_recent_trade(msg.from_user)

    bot.send_message(
        trade.seller,
        emoji.emojize(
            f"""
Trade Details
-----------------

    <b>ID --> {trade.id}</b>
    <b>Price --> {trade.price} {trade.currency}</b>
    <b>Preferred method of payment --> {trade.coin}</b>
    <b>Created on --> {trade.created_at}</b>

Share only the trade ID with your customer to allow his/her join the trade. They would receive all the related information when they join.
            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )


#############APPROVING PAYMENTS


def validate_pay(msg):
    "Receives the transaction hash for checking"
    trade = get_recent_trade(msg.from_user)

    trade_hash = msg.text

    status = check_payment(trade, trade_hash)

    if status == "Approved":

        ##SEND CONFIRMATION TO SELLER
        bot.send_message(
            trade.seller,
            emoji.emojize(
                f"""
<b>TRADE ID - {trade.id}</b>                   
<b>Buyer Payment Confirmed Successfully. Please release the goods to the buyer before being paid</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )

        ##SEND CONFIRMATION TO BUYER
        bot.send_message(
            trade.buyer,
            emoji.emojize(
                f"""
<b>TRADE ID - {trade.id}</b>      
<b>Payment Confirmed Sucessfully. Seller has been instructed to release the goods to you.</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=confirm_goods()
        )

    else:

        ##SEND ALERT TO SELLER
        bot.send_message(
            trade.buyer,
            emoji.emojize(
                f"""
<b>TRADE ID - {trade.id}</b>  
<b>Payment Still Pending! Please cross check the transaction hash and try again.</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )



##REFUND PROCESS FOR BUYER

def refund_to_buyer(msg):
    "Refund Coins Back To Buyer"
    trade = get_recent_trade(msg)

    if trade.payment_status == True:

        question = bot.send_message(
            trade.buyer,
            f"A refund was requested for your funds on trade {trade.id}. Please paste a wallet address to receive in {trade.coin}"
        )
        bot.register_next_step_handler(question, refund_coins)
    
    else:
        bot.send_message(
            msg.id,
              emoji.emojize(
                ":warning: Buyer Has Not Made Payments Yet!!",
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )

def refund_coins(msg):
    "Payout refund"

    wallet = msg.text
    trade = get_recent_trade(msg.from_user)

    pay_to_buyer(trade, wallet)

    bot.send_message(
        ADMIN_ID,
        emoji.emojize(
            """
<b>Refunds Paid</b> 
            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )



##REFUND PROCES SELLER TO RECEIVE FUNDS

def refund_to_seller(msg):
    "Refund Coins Back To Buyer"
    trade = get_recent_trade(msg)

    if trade.payment_status == True:

        pay_funds_to_seller(trade)
    
    else:
        bot.send_message(
            msg.id,
              emoji.emojize(
                ":warning: Buyer Has Not Made Payments Yet!!",
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )