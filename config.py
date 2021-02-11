import os
import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, Blueprint, make_response, request, render_template
from flask_restful import Api, Resource
from coinbase.wallet.client import Client
from dotenv import load_dotenv
load_dotenv()

# Configuration variable
TOKEN = os.getenv("TOKEN")

ADMIN_ID = os.getenv("ADMIN_ID")

# Coinbase API for payments
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

FORGING_BLOCK_TOKEN = os.getenv("FORGING_BLOCK_TOKEN")
MAIL = os.getenv("MAIL")
PASS = os.getenv("PASS")

bot = telebot.AsyncTeleBot(TOKEN, threaded=True)

import importdir
importdir.do("handlers", globals())
   