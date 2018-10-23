# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.mail import send_mail_template
from core.utils import  generate_hash_key

from .models import Trabalhos, DefesaTrabalho, BancaTrabalho
from .forms import TrabalhoForm, DefesaTrabalhoForm

from mensagem.models import EmailParticipacaoBanca

def cadastrar_trabalho(request):
	template_name = 'trabalhos/forms.html'
	context = {}
	if request.method == 'POST':
		request.POST._mutable = True
		request.POST['orientador'] = request.user.id
		form = TrabalhoForm(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.save()
			return redirect('core:home')
	else:
		form = TrabalhoForm()
	context['form'] = form
	return render(request, template_name, context)


def detalhe(request, pk):
	trabalhos = get_object_or_404(Trabalhos,pk=pk)
	context = {
		'trabalhos': trabalhos
	}

	template_name = 'trabalhos/detalhe.html'

	return render(request, template_name, context)


class TrabalhoUpdateView(UpdateView):
	template_name = 'trabalhos/editar.html'
	model = Trabalhos
	success_url = reverse_lazy(
		"core:home"
	)

	fields = [
		'titulo',
		'keywords',
		'autor',
		'co_orientador',
		'resumo'
	]
	def form_valid(self, form):
		messages.success(self.request, ("Trabalho atualizado com sucesso!"))
		return super(TrabalhoUpdateView, self).form_valid(form)


class TrabalhoDetail(APIView):
	def get_object(self, pk):
		try:
			return Trabalhos.objects.get(pk=pk)
		except Trabalhos.DoesNotExist:
			raise Http404

	def delete(self, request, pk, format=None):
		trabalho = self.get_object(pk)
		trabalho.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class DefesaTrabablhoCreate(CreateView):
	template_name = 'trabalhos/agendamento_cadastro.html'
	model = DefesaTrabalho
	form_class = DefesaTrabalhoForm
	success_url = reverse_lazy(
		"core:home"
	)

	def form_valid(self, form):
		avaliador = form.cleaned_data['banca'][0]
		self.object = form.save(commit=False)
		self.object.save()
		for user in form.cleaned_data['banca']:
			banca = BancaTrabalho.objects.create(usuario = user,defesa_trabalho = self.object)
		messages.success(self.request, ("Agendamento realizado com sucesso"))
		return super(DefesaTrabablhoCreate, self).form_valid(form)


def defesatrabalho(request, pk):

	def envia_email(defesa, user):

		key = generate_hash_key(user.name)
		email_participacao_banca = EmailParticipacaoBanca(
			remetente=request.user,
			destinatario=user,
			key=key,
			trabalho=defesa.trabalho,
			tipo='convite de participação'
		)
		email_participacao_banca.save()

		base_url = request.scheme + "://" + request.get_host()
		template_name = 'mensagem/banca/convite_participacao_banca.html'
		subject = 'Convite para compor a banca do trabalho ' + str(defesa.trabalho.titulo)
		context = {'defesa': defesa, 'base_url': base_url, 'key': key}
		send_mail_template(subject, template_name, context, [user.email], request.user.email)


	template_name = 'trabalhos/agendamento_cadastro.html'
	context = {}
	if request.method == 'POST':
		form = DefesaTrabalhoForm(request.POST)
		if form.is_valid():
			defesa = form.save(commit=False)
			defesa.save()
			for user in form.cleaned_data['banca']:
				banca = BancaTrabalho.objects.create(usuario = user, defesa_trabalho = defesa)
				envia_email(defesa, user)
			messages.success(request,'agendamento cadastrado com sucesso e convite enviado para os avaliadores')
			return redirect('core:home')
	else:
		form = DefesaTrabalhoForm(initial={'trabalho': pk, 'banca': request.user})
		print (form)
	context['form'] = form
	return render(request, template_name, context)