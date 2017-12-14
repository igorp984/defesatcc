from django.shortcuts import render

from defesa.trabalhos.models import Trabalhos

def home(request):
	trabalhos = Trabalhos.objects.all()
	template_name = 'home.html'
	context = {"trabalhos": trabalhos}

    	return render(request, template_name, context)

