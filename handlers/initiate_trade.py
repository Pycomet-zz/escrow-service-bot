from config import *
from keyboard import *
from functions import *

@bot.message_handler(regexp="^Initiate")
def open_trade(msg):
    """
    This opens a new trade with seller actions
    """
    keyboard = local_currency_menu()

    chat, id = get_received_msg(msg)
    bot.delete_message(chat.id, id)

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            ":money_bag: To create a new trade today, select which is your local currency of choice... ",
            use_aliases=True
        ),
        reply_markup=keyboard
    )



