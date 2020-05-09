from config import *
from keyboard import *
from functions import *

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
    trade = get_trade(msg.text)

    if trade != "Not Found":

        user = msg.from_user
        dispute = create_dispute(user, trade)

        bot.send_message(
            ADMIN_ID,
            emoji.emojize(
                f"""
    Dispute Report {dispute.id} - by @{msg.from_user.username}
    -----------------------------------------------------------

    <b>ID --> {trade.id}</b>
    <b>Seller ID --> {trade.seller}</b>
    <b>Buyer ID --> {trade.buyer}</b>
    <b>Price --> {trade.price} {trade.currency}</b>
    <b>Preferred method of payment --> {trade.coin}</b>
    <b>Created on --> {trade.created_at}</b>
    <b>Payment Status --> {trade.payment_status}</b>

                """,
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

        question = bot.send_message(
            msg.from_user.id,
            "What is your complaint on <b>Trade -> {msg.text}</b> ? ",
            parse_mode=telegram.ParseMode.HTML,
        )

        bot.register_next_step_handler(question, trade_complaint)

    else:
        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":warning: Trade Not Found!",
                use_aliases=True
            )
        )
    

def trade_complaint(msg):
    """
    User complaint on Trade
    """

    compliant = msg.text
    keyboard = refund_menu()

    bot.send_message(
        ADMIN_ID,
        emoji.emojize(
            """
<b>Compliant --></b> {compliant}

    Do you want to approve refund? 
            """,
            use_aliases=True
        ),
        reply_markup=keyboard,
        parse_mode=telegram.ParseMode.HTML,
    )


    bot.reply_to(
        msg,
        emoji.emojize(
            """
Your complaint has been mailed to the administrator. Please await further instructions regarding this trade.
            """,
            use_aliases=True
        )
    )