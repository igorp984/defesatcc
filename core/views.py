from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from trabalhos.models import Trabalhos

@login_required
def home(request):
	trabalhos = Trabalhos.objects.all()
	template_name = 'core/home.html'
	context = {"trabalhos": trabalhos}
	return render(request, template_name, context)

