from config import *

def main_menu():
    "Return Main Menu Keyboard"

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("I am a Seller :man:", use_aliases=True), callback_data="seller")
    b = types.InlineKeyboardButton(text=emoji.emojize("I am a Buyer :man:", use_aliases=True), callback_data="buyer")
    
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

def local_currency_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Dollars (USD)", use_aliases=True), callback_data="dollar")
    b = types.InlineKeyboardButton(text=emoji.emojize("Euros (EUR)", use_aliases=True), callback_data="euro")
    
    keyboard.add(a,b)
    return keyboard


def coin_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Bitcoin (BTC)", use_aliases=True), callback_data="btc")
    b = types.InlineKeyboardButton(text=emoji.emojize("Etherium (ETH)", use_aliases=True), callback_data="eth")
    
    keyboard.add(a,b)
    return keyboard

def refund_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Yes", use_aliases=True), callback_data="1")
    b = types.InlineKeyboardButton(text=emoji.emojize("No", use_aliases=True), callback_data="2")
    
    keyboard.add(a,b)
    return keyboard