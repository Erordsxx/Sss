import telebot, random, time, requests 
from telebot import types

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
TOKEN = ""

@bot.message_handler(commands=["start"])
def start_message(message):
	bot.send_message(
