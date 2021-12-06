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
              
Please reply with the your Group Username :grey_question: (example -> @GetGroupIDRobot)
            """,
            use_aliases=True
        )
    )
    question = question.wait()
    bot.register_next_step_handler(question, add_addresses)


def add_addresses(msg):
    
    group_id = msg.text
    chat = bot.get_chat(group_id)
    chat = chat.wait()

    agent = AgentAction().create_agent(msg.from_user.id)
    # import pdb; pdb.set_t     race()
    affiliate = create_affiliate(agent, str(chat.id))
    print(affiliate)
    if affiliate != "Already Exists":
        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":+1: Congrats!! You can now add Escrow Service(@escrowbbot) to your public group and receive your affiliate charge for trade performed by your members, selecting their roles on the group. Good Luck!!",
                use_aliases=True
            )
        )

    else:

        bot.send_message(
            msg.from_user.id,
            emoji.emojize(
                ":construction: This Group Is Already Registered",
                use_aliases=True
            )
        )




