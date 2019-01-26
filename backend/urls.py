from django.contrib import admin
from django.urls import path
from django.conf import settings
from backend.api import views
from backend.api.bot import KappaBot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query', views.QueryView.as_view()),
    path('', views.AppView.as_view()),
]

KappaBot.remove_webhook()
if (settings.KAPPA_WEBHOOK is not None):
    urlpatterns.append( path(settings.KAPPA_WEBHOOK, views.BotView.as_view()) )
    KappaBot.set_webhook(
        url=settings.KAPPA_WEBHOOK_URL + settings.KAPPA_WEBHOOK
    ) # certificate=open(settings.KAPPA_WEBHOOK_CERT, 'r')