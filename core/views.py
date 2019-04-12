from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from trabalhos.models import Trabalhos, DefesaTrabalho

@login_required
def home(request):
	template_nameHome = 'core/home.html'
	return render(request, template_nameHome)

def banca_pendente(request):
	trabalhos = Trabalhos.objects.all().filter(defesatrabalho__isnull=True)
	defesas = DefesaTrabalho.objects.all()
	list = []
	for defesa in defesas:
		avaliadores = defesa.trabalho.banca.all().exclude(bancatrabalho__status__contains='negado')
		lista = []
		for avaliador in avaliadores:
			lista.append(avaliador.name)

		defesas_dic = {
			'id': defesa.id,
			'local': defesa.local,
			'data': defesa.data,
			'hora': defesa.hora,
			'trabalho': defesa.trabalho,
			'banca': lista,
			'status': defesa.status,
		}
		list.append(defesas_dic)
		contextBanca = {"trabalhos": trabalhos, "defesas": list}
		template_nameBanca = 'core/banca_pendente.html'
	return  render(request, template_nameBanca, contextBanca)

def agendamento_pendente(request):
	trabalhos = Trabalhos.objects.all().filter(defesatrabalho__isnull=True)
	defesas = DefesaTrabalho.objects.all()
	list = []
	for defesa in defesas:
		avaliadores = defesa.trabalho.banca.all().exclude(bancatrabalho__status__contains='negado')
		lista = []
		for avaliador in avaliadores:
			lista.append(avaliador.name)

		defesas_dic = {
			'id': defesa.id,
			'local': defesa.local,
			'data': defesa.data,
			'hora': defesa.hora,
			'trabalho': defesa.trabalho,
			'banca': lista,
			'status': defesa.status,
		}
		list.append(defesas_dic)
		contextAgendamento = {"trabalhos": trabalhos, "defesas": list}
		template_nameAgendamento = 'core/agendamento_pendente.html'
	return  render(request, template_nameAgendamento, contextAgendamento)

def defesas_confirmadas(request):
	trabalhos = Trabalhos.objects.all().filter(defesatrabalho__isnull=True)
	defesas = DefesaTrabalho.objects.all()
	list = []
	for defesa in defesas:
		avaliadores = defesa.trabalho.banca.all().exclude(bancatrabalho__status__contains='negado')
		lista = []
		for avaliador in avaliadores:
			lista.append(avaliador.name)

		defesas_dic = {
			'id': defesa.id,
			'local': defesa.local,
			'data': defesa.data,
			'hora': defesa.hora,
			'trabalho': defesa.trabalho,
			'banca': lista,
			'status': defesa.status,
		}
		list.append(defesas_dic)
		contextDefesas = {"trabalhos": trabalhos, "defesas": list}
		template_nameDefesas = 'core/defesas_confirmadas.html'
	return  render(request, template_nameDefesas, contextDefesas)
