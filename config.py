import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, request

from coinbase.wallet.client import Client


# Configuration variable
TOKEN = ""


ADMIN_ID = 577180091

# Coinbase API for payments
API_KEY = ""
API_SECRET = ""
