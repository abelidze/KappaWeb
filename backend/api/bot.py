import json
import telebot
import backend.api.kira

from tabulate import tabulate
from django.conf import settings


telebot.apihelper.proxy = settings.KAPPA_PROXY
KappaBot = telebot.TeleBot(settings.KAPPA_TOKEN)


@KappaBot.message_handler(func=lambda message: True, content_types=['text'])
def process_sql(message):
    data = kira.connect().cursor().execute(message.text).fetch()
    try:
        response = json.loads(data)
        if 'columns' in response['result']:
            response = tabulate(
                response['result']['records'],
                [x['name'] for x in response['result']['columns']],
                tablefmt='presto',
                numalign='None'
            )
        else:
            response = json.dumps(response['result'])
    except:
        response = data
    KappaBot.reply_to(message, response)