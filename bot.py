from config import *
from keyboard import *
from functions import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    """
    Starting the escrow service bot
    """
    keyboard = main_menu()

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            f"""
    Hello {msg.from_user.first_name},

    :circus_tent: Welcome to the Escrow Service Bot. My purpose is to create a save trade environment for both seller and buyer subject to my rules.

    Your funds are save with me and will be refunded to you if the other party refuses to comply with the rules.
    
    What would be your role today?
            """,
            use_aliases = True
        ),
        reply_markup=keyboard
    )


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

@bot.message_handler(regexp="^Initiate")
def open_trade(msg):
    """
    This opens a new trade with seller actions
    """
    keyboard = local_currency_menu()

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            ":money_bag: You want to create trade request. Which is your local currency? ",
            use_aliases=True
        ),
        reply_markup=keyboard
    )

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
        price=price
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



@bot.message_handler(regexp="^Delete")
def delete_request(msg):
    """
    This is an option to delete trade by id
    """
    question = bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            ":warning: What is the ID of the trade ? ",
            use_aliases=True
        )
    )
    
    bot.register_next_step_handler(question, trade_delete)


def trade_delete(msg):
    """
    Deleting the trade
    """
    trade_id = msg.text

    status = delete_trade(trade_id)

    bot.send_message(
        msg.from_user.id,
        f"Deleting Trade {trade_id} {status}"
    )

######################BUYER GRID#####################

@bot.message_handler(regexp="^Join")
def join_request(msg):
    """
    Lets a user receive trade information by ID
    """
    question = bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            "What is the ID of the trade you wish to join ? ",
            use_aliases=True
        )
    )
    
    bot.register_next_step_handler(question, join_trade)

def join_trade(msg):
    """
    Validate Buyer To Trade ID
    """
    trade_id = msg.text

    trade = check_trade(
        user=msg.from_user,
        trade_id=trade_id)

    if trade != "Not Found":

        #Amount To Be Paid
        coin_price = get_price(
            coin_code=trade.coin,
            currency_code=trade.currency
        )
        service_charge = 0.01 * float(coin_price)
        fees = 2 * 0.0149

        pay_price = float(coin_price) + service_charge + float(fees)

        if trade.coin == "BTC":
            receive_wallet = btc_account.get_address().address
        elif trade.coin == "ETH":
            receive_wallet = eth_account.get_address().address


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
        <b>Payment Complete --> {trade.payment_status}</b>

:alert: <b>You are expected to pay {pay_price}{trade.coin} to {receive_wallet} to recieve goods from seller</b>

                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

    else:
        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":warning: Trade Not Found!",
                use_aliases=True
            )
        )


@bot.message_handler(regexp="^Report")
def report_request(msg):
    """
    Sends a report to the Admin regarding a particular trade
    """
    question = bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            "What is the ID of the trade you wish to report ? ",
            use_aliases=True
        )
    )
    
    bot.register_next_step_handler(question, report_trade)

def report_trade(msg):
    """
    Send reports to admin for cross checking
    """
    trade = get_recent_trade(msg.from_user)

    keyboard = refund_menu()

    bot.send_message(
        "@codefred",
        emoji.emojize(
            f"""
Trade Report From {msg.from_user.id} - {msg.from_user.username}
-----------------------------------------------------------

    <b>ID --> {trade.id}</b>
    <b>Price --> {trade.price} {trade.currency}</b>
    <b>Preferred method of payment --> {trade.coin}</b>
    <b>Created on --> {trade.created_at}</b>

            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )

    bot.send_message(
        "@codefred",
        emoji.emojize(
            "Do you want to approve refund? ",
            use_aliases=True
        ),
        reply_markup=keyboard
    )
    
    ############################################################
    # bot.register_next_step_handler(question, report_trade)








######################UNIVERSAL GRID#####################

@bot.message_handler(regexp="^Trade")
def trade_history(msg):
    """
    Return all the trades the user is involved in
    """
    user = msg.from_user

    bot.send_message(
        user.id,
        emoji.emojize(
            """
    <b>TRADE HISTORY</b>
            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )

    sells, buys = get_trades(user)

    for sell in sells:

        bot.send_message(
            user.id,
            emoji.emojize(
                f"""
<b>SELLER ROLE</b>
------------------
<b>ID --> {sell.id}</b>
<b>Price --> {sell.price} {sell.currency}</b>
<b>Preferred method of payment --> {sell.coin}</b>
<b>Created on --> {sell.created_at}</b>
<b>Payment Complete --> {sell.payment_status}</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

    for buy in buys:

        bot.send_message(
            user.id,
            emoji.emojize(
                f"""
<b>BUYER ROLE</b>
------------------
<b>ID --> {buy.id}</b>
<b>Price --> {buy.price} {buy.currency}</b>
<b>Preferred method of payment --> {buy.coin}</b>
<b>Created on --> {buy.created_at}</b>
<b>Payment Complete --> {buy.payment_status}</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )



@bot.message_handler(regexp="^Rules")
def rules(msg):
    """
    List of Rules
    """

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            f"""
<b>ESCROW SERVICE RULES</b>
---------------------------
1.  Trades can only be created by a seller.

2.  Funds deposited by the buyer are only released to seller after the goods received are affirmed by the buyer.

3.  Transaction price and trade currency should be agreed between both parties before trade is created.

4.  If a party is reported, the other party receives their refund and the guilty party banned from this service.
            """,
            use_aliases=True
        ),
        parse_mode=telegram.ParseMode.HTML,
    )



######################################################################################################


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """

    if call.data == "seller":
        start_seller(call.from_user)

    elif call.data == "buyer":
        start_buyer(call.from_user)
    
    elif call.data == "dollar":
        #create trade
        open_new_trade(call.from_user, "USD")
        select_coin(call.from_user)

    elif call.data == "euro":
        #create trade
        open_new_trade(call.from_user, "EUR")
        select_coin(call.from_user)

    elif call.data == "btc":
        #update trade information
        add_coin(
            user=call.from_user,
            coin="BTC")
        trade_price(call.from_user)
    
    elif call.data == "eth":
        #update trade information
        add_coin(
            user=call.from_user,
            coin="ETH")
        trade_price(call.from_user)

    # elif call.data == "1":
    #     #Refund
    #### CHECK TO APPROVE PAYMENTS AND REFUND/PAYMENT PROCESS

    else:
        pass





print("bot running!")
bot.polling(none_stop=True)