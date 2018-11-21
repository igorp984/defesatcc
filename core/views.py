from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from trabalhos.models import Trabalhos, DefesaTrabalho

@login_required
def home(request):
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
		}
		list.append(defesas_dic)
	template_name = 'core/home.html'
	context = {"trabalhos": trabalhos, "defesas": list}
	return render(request, template_name, context)

