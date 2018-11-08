# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from accounts.decorators import acesso, valida_perfil
from django.contrib import messages

from .serializers import UsuarioSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from core.utils import generate_hash_key

from .forms import CadastroForm, LoginForm, EditaCadastroForm, ResetSenhaForm, PerfilForm
from .models import NovaSenha, Perfil
from mensagem.models import  EmailParticipacaoBanca
from trabalhos.models import  Trabalhos, DefesaTrabalho, BancaTrabalho

Usuario = get_user_model()

# Create your views here.

def meu_login(request):
	template_name = 'accounts/login.html'
	form = LoginForm()
	context = {}
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password1'])
		if user is not None:
			login(request, user)
			return redirect('core:home')
	else:
		context['insuccess'] = True
	context = { 'form': form }
	
	return render(request, template_name, context)			


def cadastro(request, trabalho_id=None):
	template_name = 'accounts/cadastro.html'

	if request.method == 'POST':
		form = CadastroForm(request.POST)
		if form.is_valid():
			user = form.save()
			if trabalho_id:
				trabalho = Trabalhos.objects.get(pk=trabalho_id)
				key = generate_hash_key(user.name)
				email_participacao_banca = EmailParticipacaoBanca(
					remetente=trabalho.orientador,
					destinatario=user,
					key=key,
					trabalho=trabalho,
					tipo='convite de participação'
				)
				email_participacao_banca.save()

			messages.success(request,'Usuário cadastrado com sucesso')
			return redirect('core:home')
	else:
		form = CadastroForm()		
	context = {
		'form': form
	}

	return render(request, template_name, context)

def reset_senha(request):
	template_name = 'accounts/reset_senha.html'
	form = ResetSenhaForm(request.POST or None)
	context = {}
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form
	return render(request, template_name, context)


def reset_senha_confirm(request, key):
	template_name = 'accounts/reset_senha_confirm.html'
	context = {}
	reset = get_object_or_404(NovaSenha, key=key)
	form = SetPasswordForm(user=reset.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		context['success'] = True
	context['form'] = form	
	return render(request, template_name, context)	



class UsuarioUpdateView(UpdateView):
	template_name = 'accounts/editar.html'
	model = Usuario
	form_class = EditaCadastroForm


	def form_valid(self, form):
		messages.success(self.request, ("Perfil atualizado com sucesso"))
		return super(UsuarioUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse("accounts:editar", kwargs={'pk': self.get_object().id})


class UsuarioUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer


@login_required
def editar_senha(request):
	template_name = 'accounts/editar_senha.html'
	context = {}

	if request.POST == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)

	context['form'] = form
	return render(request, template_name, context)


class PerfilCreateView(CreateView):
	template_name = 'accounts/novo_perfil.html'
	model = Perfil
	form_class = PerfilForm
	success_url = reverse_lazy(
		"accounts:lista_perfis"
	)

	@method_decorator(login_required)
	@method_decorator(acesso('alto'))
	def dispatch(self, *args, **kwargs):
		return super(PerfilCreateView, self).dispatch(*args, **kwargs)