#Token 6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w


import telebot
bot = telebot.TeleBot("6156140654:AAESB4ELkinSXR4uWQVtkFTRy0zfBCX6S1w")

@bot.message_handler(commands=["start"])

def start(m, res=False):
    bot.send_message(m.chat.id, "Hello, I am David ready to test you abilties as a coder!")
    
@bot.message_handler(content_types=["text"])

def handle_text(message):
    print(message.chat.id)
    
    bot.send_message(message.chat.id, f"Your text: {message.text}")
    print(message.chat)
    
    
bot.polling(non_stop= True, interval=0 )