from config import *
from keyboard import *
from functions import *

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