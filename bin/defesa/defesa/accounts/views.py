from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from .forms import CadastroForm

# Create your views here.

def cadastro(request):
	template_name = 'accounts/cadastro.html'
	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = CadastroForm()		
	context = {
		'form': form
	}

	return render(request, template_name, context)