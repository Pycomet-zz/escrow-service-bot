from config import *
from keyboard import *
from functions import *


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
