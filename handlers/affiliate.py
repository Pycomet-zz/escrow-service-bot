from config import *
from keyboard import *
from functions import *

def start_affiliate(user):
    """
    This is the handler to start affiliate options
    """
    user = get_user(msg=user)

    question = bot.send_message(
        user.id,
        emoji.emojize(
            """
:robot: To use escrow service on your group, I would need the following information.
              
Please reply with the your Group ID :grey_question: (You can get it @GetGroupIDRobot)
            """,
            use_aliases=True
        )
    )
    question = question.wait()
    bot.register_next_step_handler(question, add_addresses)


def add_addresses(msg):
    
    group_id = msg.text

    affiliate = create_affiliate(user=msg.from_user.id, id=group_id)

    if affiliate != "Already Exists":
        question = bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                """
Please paste in your Bitcoin(BTC) receive address :grey_question:
                """,
                use_aliases=True))
        question = question.wait()
        bot.register_next_step_handler(question, add_bitcoin_space)
    
    else:

        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":construction: This Group Is Already Registered",
                use_aliases=True
            )
        )



def add_bitcoin_space(msg):
    "Add Bitcoin Address For Affiliate"
    wallet = msg.text

    user = get_user(msg=msg)

    add_affiliate_btc(
        id = user.chat,
        wallet = wallet
        )

    question = bot.send_message(
            user.id,
            emoji.emojize(
                """
Please paste in your Ethereum(ETH) receive address :grey_question:
                """,
                use_aliases=True
            )
        )

    question = question.wait()

    bot.register_next_step_handler(question, add_ethereum_space)


def add_ethereum_space(msg):
    "Add Ethereum Address For Affiliate"
    wallet = msg.text

    user = get_user(msg=msg)

    add_affiliate_eth(
        id = user.chat,
        wallet = wallet
        )
    
    question = bot.send_message(
            user.id,
            emoji.emojize(
                """
Please paste in your Litecoin(LTC) receive address :grey_question:
                """,
                use_aliases=True
            )
        )
    
    question = question.wait()

    bot.register_next_step_handler(question, add_litecoin_space)


def add_litecoin_space(msg):
    "Add Litecoin Address For Affiliate"
    wallet = msg.text
    user = get_user(msg=msg)

    add_affiliate_ltc(
        id = user.chat,
        wallet = wallet
    )

    question = bot.send_message(
            user.id,
            emoji.emojize(
                """
Please paste in your Ripplecoin(XRP) receive address :grey_question:
                """,
                use_aliases=True
            )
        )
    
    question = question.wait()

    bot.register_next_step_handler(question, add_ripplecoin_space)


def add_ripplecoin_space(msg):
    "Add Ripplecoin Address For Affiliate"
    wallet = msg.text
    user = get_user(msg=msg)

    add_affiliate_xrp(
        id = user.chat,
        wallet = wallet
    )

    question = bot.send_message(
            user.id,
            emoji.emojize(
                """
Please paste in your Bitcoin Cash(BCH) receive address :grey_question:
                """,
                use_aliases=True
            )
        )
    
    question = question.wait()

    bot.register_next_step_handler(question, add_bitcoincash_space)

def add_bitcoincash_space(msg):
    "Add Bitcoin Cash For Affiliate"
    wallet = msg.text
    user = get_user(msg=msg)

    add_affiliate_bch(
        id = user.chat,
        wallet = wallet
    )

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            ":+1: Congrats!! You can now add Escrow Service(@escrowbbot) to your public group and receive your affiliate charge for trade performed by your members, selecting their roles on the group. Good Luck!!",
            use_aliases=True
        )
    )
