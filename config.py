import os
import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, request, render_template
from coinbase.wallet.client import Client
from dotenv import load_dotenv
load_dotenv()

DEBUG = False

# Configuration variable
TOKEN = os.getenv("TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID")

# Coinbase API for payments
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

bot = telebot.AsyncTeleBot(TOKEN, threaded=True)

import importdir
importdir.do("handlers", globals())
