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

    send_trade_info(msg.from_user)



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
def join_trade(msg):
    """
    Lets a user receive trade information by ID
    """
    pass

@bot.message_handler(regexp="^Report")
def report_trade(msg):
    """
    Sends a report to the Admin regarding a particular trade
    """
    pass

######################UNIVERSAL GRID#####################

@bot.message_handler(regexp="^Trade")
def trade_history(msg):
    """
    Return all the trades the user is involved in
    """
    pass

@bot.message_handler(regexp="^Rules")
def rules(msg):
    """
    List of Rules
    """
    pass



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
        add_coin(call.from_user, "BTC")
        trade_price(call.from_user)
    
    elif call.data == "eth":
        #update trade information
        add_coin(call.from_user, "ETH")
        trade_price(call.from_user)

    else:
        pass





print("bot running!")
bot.polling(none_stop=True)