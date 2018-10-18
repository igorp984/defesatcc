# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.mail import send_mail_template
from core.utils import generate_hash_key
from trabalhos.models import Trabalhos
from .models import EmailParticipacaoBanca
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class EnviaEmailParticipacaoBanca(APIView):

    def post(self, request, pk, format=None):
        trabalho = Trabalhos.objects.get(pk=pk)
        key = generate_hash_key(request.user.username)
        email_participacao_banca = EmailParticipacaoBanca(
            remetente=request.user,
            destinatario=trabalho.orientador,
            key=key,
            trabalho=trabalho,
            tipo='pedido de participação'
        )
        email_participacao_banca.save()
        template_name = 'mensagem/banca/pedido_participacao_banca.html'
        subject = 'Solitação para compor a banca do trabalho ' + str(trabalho.titulo)
        context = {'email': email_participacao_banca}
        send_mail_template(subject, template_name, context, [trabalho.orientador.email], request.user.email)
        messages.success(request, 'Sua solicitação para participação da banca foi enviada ao orientador')
        return Response(status=status.HTTP_204_NO_CONTENT)

def resposta_participacao_banca(request, pk):

    if pk == '1':
        messages.success(request,'o orientador aceitou o convite')
        return redirect('core:home')
    else:
        messages.success(request,'o orientador negou o convite')
        return redirect('core:home')