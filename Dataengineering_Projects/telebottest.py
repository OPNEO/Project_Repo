import telebot
import random
from  datetime import datetime
from time import sleep
BOT_TOKEN = "7311657178:AAF3LQfjzlFWXwBJ5kAEC1EcC9w9Aq1FDSg"
CHANNEL_ID = "@telebotforpythondata"
try:
    bot=telebot.TeleBot(BOT_TOKEN)
    temperature = random.randint(0, 50)
    humidity = random.randint(0, 50)
    pressure = random.randint(0, 50)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = (
        f"Random Temperature \n"
        f"Temperature: {temperature}°C\n"
        f"Humidity: {humidity}%\n"
        f"Pressure: {pressure} hPa\n"
        f"Timestamp: {timestamp}"
    )
    print(message,type(message))
    bot.send_message(CHANNEL_ID,message)
except Exception as e:
    print(e)
