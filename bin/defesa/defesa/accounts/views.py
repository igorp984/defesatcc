from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import CadastroForm, EditaCadastroForm 


# Create your views here.

def cadastro(request):
	template_name = 'accounts/cadastro.html'
	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username=user.username, password=form.cleaned_data['password1'])
			login(request, user)
			return redirect('core:home')
	else:
		form = CadastroForm()		
	context = {
		'form': form
	}

	return render(request, template_name, context)

@login_required
def editar(request):
	template_name = 'accounts/editar.html'
	form = EditaCadastroForm()
	context = { 'form': form }
	
	return render(request, template_name, context)