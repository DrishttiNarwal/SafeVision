import requests

def send_telegram_image(image_file):
    bot_token = '7668192552:AAHYh4DFY89JuzeASFY6pmC_-DunP7WWUaw'
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    data = {
        'chat_id': '6486614215'
    }
    files = {
        'photo': image_file
    }
    response = requests.post(url, data=data, files=files)
    return response.json()

def send_telegram_message():
    bot_token = '7668192552:AAHYh4DFY89JuzeASFY6pmC_-DunP7WWUaw'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': '6486614215',
        'text': 'violence-detected'
    }
    response = requests.post(url, data=data)
    return response.json()

