from config import *
from keyboard import *
from functions import *


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
<b>Trade still open --> {sell.is_open}</b>

<b>Dispute Status --> {sell.is_dispute()}</b>
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
<b>Trade still open --> {buy.is_open}</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )
