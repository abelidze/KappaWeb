from django.contrib import admin
from django.urls import path
from django.conf import settings
from backend.api import views
from backend.api.bot import KappaBot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query', views.QueryView.as_view()),
    path(settings.KAPPA_WEBHOOK, views.BotView.as_view()),
    path('', views.AppView.as_view()),
]

if (settings.KAPPA_WEBHOOK is not None):
    print(settings.KAPPA_WEBHOOK_URL + settings.KAPPA_WEBHOOK)
    KappaBot.remove_webhook()
    KappaBot.set_webhook(
        url=settings.KAPPA_WEBHOOK_URL + settings.KAPPA_WEBHOOK
    ) # certificate=open(settings.KAPPA_WEBHOOK_CERT, 'r')


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