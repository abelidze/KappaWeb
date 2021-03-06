from django.apps import AppConfig
from django.conf import settings
from backend.api.bot import KappaBot

class ApiConfig(AppConfig):
    name = 'backend.api'

    def ready(self):
        if (settings.KAPPA_WEBHOOK is not None):
            print(KappaBot.remove_webhook())
            print(KappaBot.set_webhook(
                url=settings.KAPPA_WEBHOOK_URL + settings.KAPPA_WEBHOOK,
                certificate=open(settings.KAPPA_WEBHOOK_CERT, 'r')
            ))
            print(KappaBot.get_webhook_info())