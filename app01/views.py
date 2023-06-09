from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import incluirTramitacao
from django.urls import reverse
from .forms import f001_Tramitacoes
from django.contrib.auth.decorators import login_required
from accounts.models import User
import pyodbc as p
import openpyxl
import datetime
import os
import json
import mysql.connector

def sessao(request):
    if not request.session.get('username'):
        request.session['username'] = request.user.username
    return



@login_required
def v001_cadastro_tramitacoes(request):

    sessao(request)
    current_user=request.user.iduser
    if (request.method == "POST" and request.FILES['filename']):

        operacao=request.POST['operacao']
        tramitacao=request.POST['tramitacao']
        planilha=request.FILES['filename']

        if (operacao=='REAGENDAR' or operacao=='EXCLUIR'):
            incluirTramitacao.incluir(planilha,operacao,tramitacao,current_user)
        elif (operacao=='INCLUIR' or operacao=='STATUS' or operacao=='STATUS/INCLUIR'):
            incluirTramitacao.incluir(planilha,operacao,tramitacao,current_user)


        return HttpResponseRedirect(reverse('app01:cadastro_tramitacoes'))
    else:

        titulo = 'Cadastro de Tramitações'
        form = f001_Tramitacoes()
    return render(request, 'app01/tramitacoes.html',
            {
                'form':form,
                'titulo_pagina': titulo,
                'usuario':request.session['username']
            }
          )
