import os
import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, request

from coinbase.wallet.client import Client


# Configuration variable
TOKEN = os.getenv("TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID")

# Coinbase API for payments
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

bot = telebot.TeleBot(TOKEN, threaded=True)

import importdir
importdir.do("handlers", globals())
