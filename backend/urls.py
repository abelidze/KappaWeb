from django.contrib import admin
from django.urls import path
from django.conf import settings
from backend.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query', views.QueryView.as_view()),
    path('', views.AppView.as_view()),
]

if settings.KAPPA_WEBHOOK is not None:
    urlpatterns.append(path(settings.KAPPA_WEBHOOK, views.test))