from config import *
from keyboard import *
from functions import *
from bot import *

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






    elif call.data == "payment_confirmation":
        #Check payment confirmation
        question = bot.send_message(
            call.from_user.id,
            emoji.emojize(":point_right: Paste the transaction hash for confirmation below", use_aliases=True),
        )
        bot.register_next_step_handler(question, validate_pay)






    elif call.data == "goods_received":
        ### Pay The Seller
        trade = get_recent_trade(call.from_user)
        pay_funds_to_seller(trade)

        ##SEND TO SELLER
        bot.send_message(
            trade.seller,
            emoji.emojize(
                "<b>TRADE ENDED!!. Your payment has been sent!</b>",
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML
        )

        ##SEND TO BUYER
        bot.send_message(
            trade.buyer,
            emoji.emojize(
                "<b>TRADE ENDED!!</b>",
                use_aliases=True
            ),
            parse_mode=telegram.ParseMode.HTML,
        )





    elif call.data == "goods_not_received":
        #### Open Dispute
        bot.send_message(
            call.from_user.id,
            "Please contact the seller to send you the goods right away. If seller refuses, report the trade from the menu",
        )


    elif call.data == "refund":
        # Refund coins to buyer
        question = bot.send_message(
            ADMIN_ID,
            "What is the trade ID ? "
        )
        bot.register_next_step_handler(question, refund_to_buyer)



    else:
        pass

