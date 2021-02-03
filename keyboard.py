from config import *

def main_menu(msg):
    "Return Main Menu Keyboard"

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("I am a Seller :man:", use_aliases=True), callback_data="seller")
    b = types.InlineKeyboardButton(text=emoji.emojize("I am a Buyer :man:", use_aliases=True), callback_data="buyer")
    c = types.InlineKeyboardButton(text=emoji.emojize(":man: Using this service on my group :man:", use_aliases=True), callback_data="affiliate")
    
    keyboard.add(a,b)
    
    if msg.chat.type == "private":
        keyboard.add(c)
    
    return keyboard


def seller_menu():
    "Return Seller Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Initiate Trade :ledger:", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Delete Trade :closed_book:", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History :books:", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules :scroll:", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard


def buyer_menu():
    "Return Buyer Options"

    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton(emoji.emojize("Join Trade :memo:", use_aliases=True))
    b = types.KeyboardButton(emoji.emojize("Report Trade :open_file_folder:", use_aliases=True))
    c = types.KeyboardButton(emoji.emojize("Trade History :books:", use_aliases=True))
    d = types.KeyboardButton(emoji.emojize("Rules :scroll:", use_aliases=True))

    keyboard.add(a,b,c,d)
    return keyboard

def local_currency_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize(":dollar: US Dollars (USD)", use_aliases=True), callback_data="dollar")
    b = types.InlineKeyboardButton(text=emoji.emojize(":euro: Euros (EUR)", use_aliases=True), callback_data="euro")
    c = types.InlineKeyboardButton(text=emoji.emojize(":pound: British Pound (EUR)", use_aliases=True), callback_data="pound")
    d = types.InlineKeyboardButton(text=emoji.emojize(":dollar: Canadian Dollar (CAD)", use_aliases=True), callback_data="c_dollar")
    e = types.InlineKeyboardButton(text=emoji.emojize(":yen: Japanese Yen (JPY)", use_aliases=True), callback_data="yen")
    f = types.InlineKeyboardButton(text=emoji.emojize(":euro: Swiss Franc (CHF)", use_aliases=True), callback_data="swiss")
    
    keyboard.add(a,b,c,d,e,f)
    return keyboard


def coin_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Bitcoin (BTC)", use_aliases=True), callback_data="btc")
    b = types.InlineKeyboardButton(text=emoji.emojize("Ethereum (ETH)", use_aliases=True), callback_data="eth")
    
    keyboard.add(a,b)
    return keyboard

def give_verdict():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = types.InlineKeyboardButton(text=emoji.emojize("Yes :+1:", use_aliases=True), callback_data="verdict")
    b = types.InlineKeyboardButton(text=emoji.emojize("No :-1:", use_aliases=True), callback_data="2")
    
    keyboard.add(a,b)
    return keyboard

def confirm():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(":money_bag: Confirm Payment", use_aliases=True), callback_data="payment_confirmation")
    keyboard.add(a)
    return keyboard

def confirm_goods():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize("Received :white_check_mark:", use_aliases=True), callback_data="goods_received")
    b = types.InlineKeyboardButton(text=emoji.emojize("Not Received :x:", use_aliases=True), callback_data="goods_not_received")
    keyboard.add(a, b)
    return keyboard

def refunds():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text=emoji.emojize(":man: To Buyer", use_aliases=True), callback_data="refund_to_buyer")
    b = types.InlineKeyboardButton(text=emoji.emojize(":man: To Seller", use_aliases=True), callback_data="pay_to_seller")
    c = types.InlineKeyboardButton(text=emoji.emojize(" :closed_lock_with_key: Close Trade", use_aliases=True), callback_data="close_trade")
    keyboard.add(a, b, c)
    return keyboard