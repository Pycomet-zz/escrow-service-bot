from config import *
import os
server = Flask(__name__)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://escrowbbot.herokuapp.com/' + TOKEN)
    return "!", 200



print("bot polling...")
# bot.remove_webhook()
bot.polling(none_stop=True)

# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))




    