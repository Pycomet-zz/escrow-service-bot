from config import *
from keyboard import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    """
    Starting the escrow service bot
    """
    keyboard = main_menu()

    bot.send_message(
        msg.from_user.id,
        emoji.emojize(
            f"""
    Hello {msg.from_user.first_name},

    :circus_tent: Welcome to the Escrow Service Bot. My purpose is to create a save trade environment for both seller and buyer subject to my rules.
    Your funds are save with me and will be refunded to you if the other party refuses to comply with the rules. What would be your role today?
            """,
            use_aliases = True
        ),
        reply_markup=keyboard
    )

print("bot running!")
bot.polling(none_stop=True)