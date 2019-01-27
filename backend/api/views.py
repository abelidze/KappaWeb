import backend.api.kira as kira
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views import View
from telebot.types import Update
from backend.api.bot import KappaBot


class AppView(View):
	template_name = 'index.html'

	def get(self, request):
		return render(request, self.template_name, {})


@method_decorator(csrf_exempt, name='dispatch')
class QueryView(View):
	def post(self, request):
		conn = kira.connect()
		response = HttpResponse()
		response.content = conn.cursor().execute(request.body).fetch()
		return response


@method_decorator(csrf_exempt, name='dispatch')
class BotView(View):
    def post(self, request):
        print(request.body)
        if request.content_type == 'application/json':
            update = Update.de_json(request.body.encode('utf-8'))
            KappaBot.process_new_updates([update])
        return HttpResponse(status=200)

@method_decorator(csrf_exempt, name='dispatch')
def test(request):
    print(request.body)
    return HttpResponse(status=200)