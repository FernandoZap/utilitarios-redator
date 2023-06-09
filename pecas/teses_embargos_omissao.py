# -*- coding: utf-8 -*-

import os
import datetime
from . import funcoes_gerais
from docx.shared import RGBColor

def teseConstrutor(dados_compl, dados_pasta,tese,doc):
    publicando_nome = dados_pasta['publicando_nome']
    publicando_oab =  'OAB: '+dados_pasta['publicando_oab']
    elementos = []
    if tese=='tese1':
        doc.add_paragraph('DA TEMPESTIVIDADE')
    if tese=='tese2':
        doc.add_paragraph('Inicialmente, cumpre observar que foi publicado dia [data_public], no Diário da Justiça Eletrônico, a r. decisão exarada, como se verifica na colação abaixo:')
    return doc


