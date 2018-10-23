from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from trabalhos.models import Trabalhos, DefesaTrabalho

@login_required
def home(request):
	trabalhos = Trabalhos.objects.all()
	defesas = DefesaTrabalho.objects.all()
	list = []
	for defesa in defesas:
		avaliadores = defesa.banca.all()
		lista = []
		for avaliador in avaliadores:
			lista.append(avaliador.name)

		defesas_dic = {
			'local': defesa.local,
			'data': defesa.data,
			'hora': defesa.hora,
			'trabalho': defesa.trabalho.titulo,
			'banca': lista
		}
		list.append(defesas_dic)

	template_name = 'core/home.html'
	context = {"trabalhos": trabalhos, "defesas": list}
	return render(request, template_name, context)

