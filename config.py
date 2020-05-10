import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, request

from coinbase.wallet.client import Client


# Configuration variable
TOKEN = "1222989785:AAE-o7ayaLOKr3Cw_O_3PKSeJ2jtgT6VB04"


ADMIN_ID = 577180091

# Coinbase API for payments
API_KEY = "x0zSLqHir18lLzlZ"
API_SECRET = "g04EhUsja3HXcnQYf79Ga2s7tBbWGrxi"

bot = telebot.TeleBot(TOKEN, threaded=True)

import importdir
importdir.do("handlers", globals())
