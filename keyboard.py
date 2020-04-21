from config import *

def main_menu():
    "Return Main Menu Keyboard"

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(emoji.emojize("I am a Seller :man:", use_aliases=True))
    b = types.InlineKeyboardButton(emoji.emojize("I am a Buyer :man:", use_aliases=True))
    
    keyboard.add(a,b)
    return keyboard


def seller_menu():
    "Return Seller Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Initiate Trade", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Delete Trade", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard


def buyer_menu():
    "Return Buyer Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Join Trade", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Report Trade", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard

