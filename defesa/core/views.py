from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from defesa.trabalhos.models import Trabalhos

@login_required
def home(request):
	trabalhos = Trabalhos.objects.all()
	template_name = 'home.html'
	context = {"trabalhos": trabalhos}
	return render(request, template_name, context)

