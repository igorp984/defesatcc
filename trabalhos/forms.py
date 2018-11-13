# -*- coding: utf-8 -*-
from django import forms

from .models import Trabalhos, DefesaTrabalho
from accounts.models import Usuario

class TrabalhoForm(forms.ModelForm):

	titulo = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Título do Trabalho'}),max_length=150)
	keywords = forms.CharField(label='Palavras Chaves',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite as palavras Chaves'}) ,max_length=150)
	autor = forms.CharField(label='Autor', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do Autor'}),max_length=150)
	orientador = forms.ModelChoiceField(label='Orientador',queryset=Usuario.objects.order_by('name'), widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
	co_orientador = forms.CharField(label='Co-Orientador', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do Co-Orientador'}), max_length=150, required=False)
	resumo = forms.CharField(label='Resumo', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite o Resumo do Trabalho'}), required=False)
	pdf_trabalho = forms.FileField(label='Filer', widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
	class Meta:
		model = Trabalhos
		fields = ('titulo', 'keywords', 'autor', 'orientador', 'co_orientador', 'resumo', 'pdf_trabalho')


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
			'hora': forms.TextInput(attrs={'class': 'timepicker'})
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
