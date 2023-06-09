from  django.urls import include, path
from django.contrib import admin
from . import views as v1

app_name = 'app01'

urlpatterns = [
    path('tramitacoes', v1.v001_cadastro_tramitacoes, name='cadastro_tramitacoes'),
]
