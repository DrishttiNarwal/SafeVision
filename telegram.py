import os
import requests

from dotenv import load_dotenv
load_dotenv()  # loads environment variables from .env

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram_image(image_file):
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    data = {
        'chat_id': chat_id
    }
    files = {
        'photo': image_file
    }
    response = requests.post(url, data=data, files=files)
    return response.json()

def send_telegram_message():
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': 'violence-detected'
    }
    response = requests.post(url, data=data)
    return response.json()

print("BOT TOKEN:", bot_token)
print("CHAT ID:", chat_id)
