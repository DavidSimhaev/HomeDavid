#Token 6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w


import telebot, wikipedia

bot = telebot.TeleBot("6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w")

from wikigettext import getwiki
wikipedia.set_lang("ru")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Что мне для вас найти?")
    
    
    
@bot.message_handler(content_types=["text"])

def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    
    
    
bot.polling(non_stop=True, interval=0)