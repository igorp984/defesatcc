# -*- coding: utf-8 -*-
from django import forms

from .models import Trabalhos, DefesaTrabalho
from accounts.models import Usuario


class TrabalhoForm(forms.ModelForm):

	class Meta:
		model = Trabalhos
		fields = ('titulo', 'keywords', 'autor', 'orientador', 'co_orientador', 'resumo', 'pdf_trabalho')
		widgets = {
			'orientador': forms.Select(attrs={'disabled': 'disabled'})
		}

class TrabalhoBancaForm(forms.ModelForm):
	class Meta:
		model = Trabalhos
		fields = ('banca',)


class DefesaTrabalhoForm(forms.ModelForm):

	class Meta:
		model = DefesaTrabalho
		exclude = ('status',)
		widgets = {
		 	'data': forms.TextInput(attrs={'class': 'datepicker'}),
			'hora': forms.TextInput(attrs={'class': 'timepicker'}),
			'trabalho': forms.Select(attrs={'disabled': 'disabled'})
		}

	# def clean(self):
	# 	cleaned_data = super(DefesaTrabalhoForm, self).clean()
	# 	banca = cleaned_data.get('banca')
	#
	# 	if len(banca) !=3 :
	# 		self.add_error('banca',
	# 			forms.ValidationError(
	# 								  ("A banca não poder ter um número de professores convidados diferente de 3")
	# 			))
