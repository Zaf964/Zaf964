
from httpx import ConnectTimeout
import asyncio
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import config
import funcs
import Test
import time
import httpx
import httpcore
from params import bot, Msg, wmsg, chatbot, chat_id

"""
def delete_messages(message):
    for i in range(message.message_id - 1, 0, -1):
        if i != 0:
            bot.delete_message(message.chat.id, i)
"""

"""init chat"""
@bot.message_handler(commands=["start"])
def start(message):
    start_buttons = ["Today Matches", "Tomorrow Matches"]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
 
    # funcs.jail()
    bot.send_message(message.chat.id, "Welcome to the best betting bot in the world! \n\n Choose an option bellow:\n\n if you are interested on the bot accuracy, feel free to buy it. 400 usd for lifetime use and enjoy making money every day \n\n High accuracy == deserve high cost\n\n @Aligator_4", reply_markup=keyboard)  
  
    
     
def main():
    while True:
        try:
            bot.polling()
        except KeyboardInterrupt:
            break
        except httpx.ConnectTimeout as e:
            print("Connection timeout occurred:", e)
            time.sleep(5)  # Add a delay of 5 seconds before retrying
        except httpcore.ConnectError as e:
            print("Connection error occurred:", e)
            time.sleep(3)  # Add a delay of 3 seconds before retrying
        except Exception as e:
            print("Error occurred:", e)
        except httpx.ConnectTimeout as e:  # Add this line to catch httpx.ConnectTimeout
            print("HTTPX connection timeout occurred:", e)

if __name__ == "__main__":
    asyncio.run(main())    

"""Engine"""
@bot.message_handler(func=lambda m: True)
def Eng(message):
    """passing arg to eng"""
    funcs.fr(message)
    






