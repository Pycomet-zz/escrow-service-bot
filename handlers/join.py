from config import *
from keyboard import *
from functions import *


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
        coin_price = get_coin_price(
            coin_code=trade.coin,
            currency_code=trade.currency
        )

        coin_value = float(trade.price)/float(coin_price)

        service_charge = 0.02 * float(coin_value)
        fees = (0.0149 * coin_value) * 2

        pay_price = float(coin_value) + service_charge + float(fees)

        price = "%.4f" % pay_price

        receive_wallet = get_receive_address(trade)

        #SEND TO BUYER########
        bot.send_message(
            trade.buyer,
            emoji.emojize(
                f"""
:memo: <b>Trade Details</b> :memo:
-----------------------------------

    :beginner: <b>ID --> {trade.id}</b>
    :beginner: <b>Price --> {trade.price} {trade.currency}</b>
    :beginner: <b>Preferred method of payment --> {trade.coin}</b>
    :beginner: <b>Created on --> {trade.created_at}</b>
    :beginner: <b>Payment Complete --> {trade.payment_status}</b>

:point_right: <b>You are expected to pay {price} {trade.coin} to wallet address below to recieve goods from seller</b>

:point_right: {receive_wallet}

                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=confirm(),
        )

        ##SEND ALERT TO SELLER#########
        bot.send_message(
            trade.seller,
            emoji.emojize(
                "<b>Buyer Just Joined Trade!!</b>",
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )

    else:
        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":warning: Trade Not Found!",
                use_aliases=True
            )
        )

