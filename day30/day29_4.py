#Token 6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w


import telebot
import os
from brain import answer
bot = telebot.TeleBot("6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w")


mas = []
if os.path.exists("brain.txt"):
    f = open("brain.txt", "r", encoding="UTF-8")
    for x in f:
        if len(x.strip())>2:
            mas.append(x.strip().lower())
            


@bot.message_handler(commands=["start"])

def start(m, res=False):
    bot.send_message(m.chat.id, "Давай погорим? Задай мне вопрос!")
    
@bot.message_handler(content_types=["text"])

def handle_text(message):
    print(message.chat.id)
    
    bot.send_message(message.chat.id, answer(message.text, mas))
    print(message.chat)
    
    
bot.polling(non_stop= True, interval=0 )