
####ADMIN JUDGEMENT ON TRADE
from config import *
from keyboard import *
from functions import *

trade = ""

@bot.message_handler(commands=['disputes'])
def start_dispute(msg):
    "Starts The Ticket Review Session"

    question = bot.send_message(
        ADMIN_ID,
        emoji.emojize("What is the Dispute ID :grey_question:", use_aliases=True)
    )
    bot.register_next_step_handler(question, call_dispute)



def call_dispute(msg):
    """Send The Verdict To Buyer And Seller"""

    global trade
    dispute_id = msg.text

    dispute = get_dispute_by_id(dispute_id)
    keyboard = give_verdict()

    trade = dispute.trade

    if dispute != "No Dispute":

        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                f"""
:ticket: <b>Dispute Ticket -- {dispute.id}</b>
----------------------
Complaint --> {dispute.complaint}


Trade Info;
-------------
<b>ID --> {trade.id}</b>
<b>Seller ID --> {trade.seller}</b>
<b>Buyer ID --> {trade.buyer}</b>
<b>Price --> {trade.price} {trade.currency}</b>
<b>Preferred method of payment --> {trade.coin}</b>
<b>Created on --> {trade.created_at}</b>
<b>Payment Status --> {trade.payment_status}</b>
<b>Is Open --> {trade.is_open}</b>

Give verdict :grey_question:
                """,
                use_aliases=True
            ),
            reply_markup=keyboard,
            parse_mode=telegram.ParseMode.HTML,
        )

    else:
        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":warning: Dispute Not Found!",
                use_aliases=True
            )
        )




def pass_verdict(msg):
    """This Would Send The Admin Verdict To Both Parties Of The Trade"""
    message = msg.text

    users = [
        trade.seller,
        trade.buyer,
        msg.from_user.id,
    ]

    for user in users:

        bot.send_message(
            user,
            emoji.emojize(
                """
:ticket: <b>Administrative Decision On Trade %s</b>
-----------------------------------------
Ticket ID --> %s

%s
                """ % (trade.id, trade.dispute[0].id, message),
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )

    bot.send_message(
        msg.from_user.id,
        "Who receives the funds :grey_question:",
        reply_markup=refunds()
    )
