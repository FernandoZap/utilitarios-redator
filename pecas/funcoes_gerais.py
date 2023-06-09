from datetime import date
from num2words import num2words
import datetime

teses_embargos = {
    'TESE_NULIDADE':"N",
    'TESE_INTIMACAO_DO_MP':"N",
    'TESE_COISA_JULGADA':"N",
    'TESE_PEREMPCAO':"N",
    'TESE_LITISPENDENCIA':"N",
    'TESE_ED_OMISSAO_PRESCRICAO':"N",
    'TESE_OMISSAO_PAGAMENTO_ADM':"N",
    'TESE_OMISSAO_INADIMPLENTE':"N",
    'TESE_OMISSAO_LESAO_PRE_EXISTENTE':"N",
    'TESE_OMISSAO_REGULACAO_8':"N",
    'TESE_OMISSAO_DOS_JUROS':"N",
    'TESE_OMISSAO_DE_CORRECAO_MONETARIA':"N",
    'TESE_ULTRAPETITA':'N'
}


def f002_teses_embargos_omissao(respostas,teses):
    if respostas['intimacao_mp']=='N':
        teses['tese2']='S'

    if respostas['cj_peremp_litisp']=='1':
        teses['tese3']='S'
    elif respostas['cj_peremp_litisp']=='2':
        teses['tese4']='S'
    elif respostas['cj_peremp_litisp']=='3':
        teses['tese5']='S'

    if respostas['prescricao']=='S':
        teses['tese6']='S'

    if respostas['pagamento_adm']=='N':
        teses['tese7']='S'

    if respostas['prop_inadimp_com_pagto_Adm']=='N':
        teses['tese8']='S'

    if respostas['lesao_pre']=='S':
        teses['tese9']='S'

    if respostas['omissao']=='S':
        teses['tese10']='S'

    if respostas['juros_citacao']=='2':
        teses['tese11']='S'

    if respostas['correcao']=='2':
        teses['tese12']='S'
    return teses


def f002_teses_embargos_ultrapetita(respostas,teses):
    if respostas['tese_ultrapetita']=='S':
        teses['TESE_ULTRAPETITA']='S'
    return teses


def f002_teses_embargos_contradicao(respostas,teses):
    if respostas['valor_inferior']=='N':
        teses['tese2']='S'
    if respostas['valor_perc']=='N':
        teses['tese3']='S'
    if respostas['gradacao_superior']=='S':
        teses['tese4']='S'
    if respostas['juros_citacao']=='N':
        teses['tese5']='S'
    if respostas['correcao_monetaria']=='N':
        teses['tese6']='S'
    return teses


def local_e_data(comarca):
    dados = str(date.today()).split('-')
    ano=dados[0]
    mes=dados[1]
    dia=dados[2]
    smes=mes_extenso(int(mes))
    return comarca.capitalize() + ', '+dia+' de '+smes+' de '+ano

def mes_extenso(mes):
    meses = {1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}
    return meses[mes]

def f003_teses():
    teses=teses_embargos
    teses['TESE_INTIMACAO_DO_MP']='S'
    teses['TESE_COISA_JULGADA']='S'
    teses['TESE_PEREMPCAO']='S'
    teses['TESE_LITISPENDENCIA']='S'
    teses['TESE_ED_OMISSAO_PRESCRICAO']='S'
    teses['TESE_OMISSAO_PAGAMENTO_ADM']='S'
    teses['TESE_OMISSAO_INADIMPLENTE']='S'
    teses['TESE_OMISSAO_LESAO_PRE_EXISTENTE']='S'
    teses['TESE_OMISSAO_REGULACAO_8']='S'
    teses['TESE_OMISSAO_DOS_JUROS']='S'
    teses['TESE_OMISSAO_DE_CORRECAO_MONETARIA']='S'
    return teses

inserir_tese = {
    'TESE_NULIDADE':"N",
    'TESE_INTIMACAO_DO_MP':"N",
    'TESE_COISA_JULGADA':"N",
    'TESE_PEREMPCAO':"N",
    'TESE_LITISPENDENCIA':"N",
    'TESE_ED_OMISSAO_PRESCRICAO':"N",
    'TESE_OMISSAO_PAGAMENTO_ADM':"N",
    'TESE_OMISSAO_INADIMPLENTE':"N",
    'TESE_OMISSAO_LESAO_PRE_EXISTENTE':"N",
    'TESE_OMISSAO_REGULACAO_8':"N",
    'TESE_OMISSAO_DOS_JUROS':"N",
    'TESE_OMISSAO_DE_CORRECAO_MONETARIA':"N"
}



def convert_data_br(data_us):
    ano = str(data_us[0:4])
    mes = str(data_us[5:7])
    dia = str(data_us[-2:])
    return dia+'/'+mes+'/'+ano


def number_to_long_number(number_p):
    if number_p.find(',')!=-1:
        number_p = number_p.split(',')
        number_p1 = int(number_p[0].replace('.',''))
        number_p2 = int(number_p[1])
    else:
        number_p1 = int(number_p.replace('.',''))
        number_p2 = 0

    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'

    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'

    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''

    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2) 
    else: 
        text2 = ''

    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2

    return result

def data_doc():
    data = str(datetime.datetime.now().today())[0:19]
    data = data.replace("-","")
    data = data.replace(":","")
    data = data[-6:]
    return data



def valor_por_extenso(number_p):
    retorno=''
    if number_p!='':
        retorno=number_to_long_number(number_p)
        if retorno[0:3]=='mil':
            retorno = 'um '+retorno
            retorno = retorno.capitalize()
    return retorno


def formatMilhar(valor):
    if valor=='':
        return valor
    elif valor is None:
        return valor
    if valor<0:
        valor=valor*(-1)
        sinal='-'
    else:
        sinal=''

    vd = f"{valor:,.2f}"
    vd = vd.replace('.','-')
    vd = vd.replace(',','.')
    vd = vd.replace('-',',')
    return sinal+vd


