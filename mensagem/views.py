# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from core.mail import send_mail_template
from core.utils import generate_hash_key
from trabalhos.models import Trabalhos, DefesaTrabalho, BancaTrabalho
from .models import EmailParticipacaoBanca

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import  date

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
        base_url = request.scheme + "://" + request.get_host()
        email_participacao_banca.save()
        template_name = 'mensagem/banca/pedido_participacao_banca.html'
        subject = 'Solitação para compor a banca do trabalho ' + str(trabalho.titulo)
        context = {'trabalho': trabalho, 'base_url': base_url, 'key': key}
        send_mail_template(subject, template_name, context, [trabalho.orientador.email], request.user.email)
        return Response(status=status.HTTP_204_NO_CONTENT)

def confirma_participacao_banca(request, key):

        participacao_banca = get_object_or_404(EmailParticipacaoBanca, key=key)

        if participacao_banca.visualizada:
            messages.error(request, 'Esta mensagem já foi respondida')
            return redirect('core:home')
        else:
            defesa_trabalho = DefesaTrabalho.objects.get(trabalho=participacao_banca.trabalho_id)
            if participacao_banca.tipo == 'pedido de participação':
                banca = BancaTrabalho(
                    usuario=participacao_banca.remetente,
                    defesa_trabalho=defesa_trabalho,
                )
                banca.status = 'aceito_pelo_orientador'
            else:
                banca = defesa_trabalho.bancatrabalho_set.get(usuario=participacao_banca.destinatario)
                banca.status = 'aceito_pelo_avaliador'
            banca.save()
            participacao_banca.visualizada = date.today()
            participacao_banca.save()
            agendado = BancaTrabalho.objects.filter(status__contains='aceito').count()
            if agendado == defesa_trabalho.bancatrabalho_set.all().count():
                defesa_trabalho.status = 'agendado'
                defesa_trabalho.save()

            messages.success(request,'Confirmação realizada com sucesso')
            return redirect('core:home')