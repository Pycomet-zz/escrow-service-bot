from config import *
from keyboard import *
from functions import *


@bot.message_handler(regexp="^Trade")
def trade_history(msg):
    """
    Return all the trades the user is involved in
    """
    user = msg.from_user
    sells, buys = get_trades(user)

    if sells == [] and buys == []:
        bot.send_message(
            user.id,
            emoji.emojize(
                """
        <b>NO TRADE HISTORY</b>
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

    else:
        
        bot.send_message(
            user.id,
            emoji.emojize(
                """
        <b>TRADE HISTORY</b> :book:
                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

        for sell in sells:

            bot.send_message(
                user.id,
                emoji.emojize(
                    f"""
<b>SELLER ROLE</b> :man:
------------------
<b>ID --> {sell.id}</b>
<b>Price --> {sell.price} {sell.currency}</b>
<b>Preferred method of payment --> {sell.coin}</b>
<b>Created on --> {sell.created_at}</b>
<b>Payment Complete --> {sell.payment_status}</b>
<b>Trade still open --> {sell.is_open}</b>
<b>Affiliate ID --> {sell.affiliate_id}</b>

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
<b>BUYER ROLE</b> :man:
------------------
<b>ID --> {buy.id}</b>
<b>Price --> {buy.price} {buy.currency}</b>
<b>Preferred method of payment --> {buy.coin}</b>
<b>Created on --> {buy.created_at}</b>
<b>Payment Complete --> {buy.payment_status}</b>
<b>Trade still open --> {buy.is_open}</b>
<b>Affiliate ID --> {buy.affiliate_id}</b>

<b>Dispute Status --> {buy.is_dispute()}</b>
                    """,
                    use_aliases=True
                ),
                parse_mode=telegram.ParseMode.HTML,
            )
