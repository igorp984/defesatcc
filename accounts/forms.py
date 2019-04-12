# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from core.mail import send_mail_template
from core.utils import generate_hash_key

from .models import NovaSenha, Titulo, Perfil

Usuario = get_user_model()


class LoginForm(forms.ModelForm):
	username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = Usuario
		fields = ['username', 'password1']

class CadastroForm(forms.ModelForm):
	username = forms.CharField(label='Usuário',widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Usuário'}))
	name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Nome'}))
	titulo = forms.ModelChoiceField(
		label='Titulação', 
		queryset=Titulo.objects.order_by('descricao'), 
		widget=forms.Select(attrs={'class':'form-control form-control-user', 'placeholder':'Selecione'})
	)
	perfil = forms.ModelChoiceField(
		label='Perfil',
		queryset=Perfil.objects.exclude(descricao='Coordenador').order_by('descricao'),
		widget=forms.Select(attrs={'class': 'form-control form-control-user', 'placeholder': 'Selecione'})
	)
	email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class':'form-control  form-control-user','placeholder':'E-mail'}))

	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder': 'Senha'}))

	password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput(attrs={'class':'form-control form-control-user','placeholder': 'Confirmar senha'}))
	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	if User.objects.filter(email=email).exists():kk
	# 		raise forms.ValidationError('Já existe usuario com este E-mail')
	# 	return email

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('A confirmação não está correta')
		return password2	

	def save(self, commit=True):
		user = super(CadastroForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.titulo = self.cleaned_data['titulo']
		user.perfil = self.cleaned_data['perfil']
		if commit:
			user.save()
		return user	

	class Meta:
		model = Usuario
		fields = ['username', 'name', 'email']	


class EditaCadastroForm(forms.ModelForm):
	# titulo = forms.ModelChoiceField(
	# 	label='Titulação',
	# 	queryset=Titulo.objects.order_by('descricao'),
	# 	widget=forms.Select(attrs={'class': 'select-wrapper', 'placeholder': 'Selecione'})
	# )
	# def clean_email(self):
	# 	email = self.cleaned_data['email']
	# 	queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
	# 	if queryset.exists():
	# 		raise forms.ValidationError('Já existe usuario com este E-mail')
	# 	return email


	class Meta:
		model = Usuario
		fields = ['titulo', 'name', 'email']


class ResetSenhaForm(forms.Form):

	email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control form-control-user'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		if Usuario.objects.filter(email=email).exists():
			return email
		raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

	def save(self):
		user = Usuario.objects.get(email=self.cleaned_data['email'])
		key = generate_hash_key(user.username)
		reset = NovaSenha(key=key, user=user)
		reset.save()
		base_url = self.scheme + "://" + self.get_host()
		template_name = 'accounts/reset_senha_mail.html'
		subject = 'Criar nova Senha no Defesas Ufba'
		context = { 'reset': reset, 'base_url': base_url}
		send_mail_template(subject, template_name, context, [user.email])

class PerfilForm(forms.ModelForm):
	
	class Meta:
		model = Perfil
		fields = [
			'descricao',
			'nivel_acesso',
		]



