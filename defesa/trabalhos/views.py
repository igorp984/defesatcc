from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages

from .models import Trabalhos
from .forms import TrabalhoForm

def cadastrar_trabalho(request):
	template_name = 'forms.html'
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

	template_name = 'detalhe.html'

	return render(request, template_name, context)


class TrabalhoUpdateView(UpdateView):
	template_name = 'editar.html'
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