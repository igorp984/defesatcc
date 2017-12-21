# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_usuario_model

Usuario = get_usuario_model()

class CadastroUsuarioForm(forms.ModelForm):

	email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Email'})
	password1 = forms.CharField(label='Senha', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'})
	password2 = forms.CharField(label='Confirmação de Senha', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'})

	def