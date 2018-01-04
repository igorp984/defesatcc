# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):

	username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class':'form-control'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Já existe usuario com este E-mail')
		return email

	def save(self, commit=True):
		user = super(CadastroForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user	


class EditaCadastroForm(forms.ModelForm):
	
	username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
		if queryset.exists():
			raise forms.ValidationError('Já existe usuario com este E-mail')
		return email

	class Meta:
		model = User
		fields = ['username', 'email']	