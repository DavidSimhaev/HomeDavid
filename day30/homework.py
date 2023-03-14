#Token 6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w

from solver import solve
import telebot
import os
from brain import answer
bot = telebot.TeleBot("6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w")
@bot.message_handler(commands=["start"])
def start(m, res = False):
    bot.send_message(m.chat.id, "Please enredr what do you to calculate")


@bot.message_handler(content_types=["text"])

def handle_text(messange):
    try:
        s = solve(messange.text)
        bot.send_message(messange.chat.id, s)
    except Exception as e:
        bot.send_message(messange.chat.id, repr(e))
        
        
bot.polling(non_stop= True, interval=0)
        
    

