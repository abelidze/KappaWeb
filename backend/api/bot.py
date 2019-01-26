import json
import telebot
import backend.api.kira

from tabulate import tabulate
from django.conf import settings


telebot.apihelper.proxy = settings.KAPPA_PROXY
KappaBot = telebot.TeleBot(settings.KAPPA_TOKEN)
