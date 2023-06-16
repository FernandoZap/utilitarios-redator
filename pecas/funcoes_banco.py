import pyodbc as p
import os
import json
import mysql.connector
#import MySQLdb # para o MySQL
from . import stringConnexao


def f001_sql(cod_pasta,flag):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()

    if flag==1:
        sql_command =   """
            select top 1 p.pasta,p.cod_cliente,
            dbo.desc_autor(p.id_pasta,'NOME') as autor,
            dbo.desc_comarca(p.id_comarca) as comarca,
            dbo.desc_estado(p.id_estado) as uf,
            p.orgao,
            p.num_orgao,
            dbo.desc_juizo(p.num_orgao,p.orgao) as juizo,
            case when secao in ('A','B') then ' - SEÇAO '+secao else '' end as secao,
            p.nr_processo,
            c.empresa as reu,
            'OAB/'+f.uf+' '+f.oab as oabJB,
            t01_nome as publicando_nome,t01_oab as publicando_oab,t01_sexo as publicando_sexo,
            ad.nome as conveniado_nome,
            'OAB/'+ad.estoab+' '+ ad.oab as conveniado_oab,
            p.id_pasta,p.tipo_sistema,
            p.coberturap,
            p.dat_citacao,
            p.dat_distribuicao,
            (select num_processoSE from processoSE se where se.id_pasta=p.id_pasta) as nr_processoSE
            from pastas p left join clientes c on c.id_cliente=p.id_cliente
                 left join cnpjuf f on f.id_estado=p.id_estado
                 left join publicando pub on pub.t01_id=p.id_publicando
                 left join advogados ad on ad.id_advogado=p.id_adv_conveniado
            where (p.pasta=? or p.cod_cliente=?)
            order by p.id_pasta desc
        """

    try:
        db_cursor.execute(sql_command, [cod_pasta,cod_pasta])
        row = db_cursor.fetchone()

        dados = {
            'pasta':row[0],
            'cod_cliente':row[1],
            'autor':row[2],
            'comarca':row[3],
            'uf':row[4],
            'orgao':row[5],
            'num_orgao':row[6],
            'juizo':row[7],
            'secao':row[8],
            'nr_processo':row[9],
            'reu':row[10],
            'oabJB':row[11],
            'publicando_nome':row[12],
            'publicando_oab':row[13],
            'publicando_sexo':row[14],
            'conveniado_nome':row[15],
            'conveniado_oab':row[16],
            'id_pasta':row[17],
            'tipo_sistema':row[18],
            'coberturap':row[19],
            'dat_citacao':row[20],
            'dat_distribuicao':row[21],
            'nr_processoSE':row[22]
        }

        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")

    return dados

def f001_mysql(cod_pasta):

    db_connection = MySQLdb.connect(host="", user="", passwd="", db="")
    db_cursor = db_connection.cursor()
    sql_command =   """
        select 
        pasta,
        cod_cliente,
        autor,
        comarca,
        estado,
        orgao,
        num_orgao,
        CASE WHEN orgao='Vara-Civel' THEN 'DA' ELSE 'DO' END AS preposicao,
        cobertura,
        ifnull(secao,'') as secao,
        nr_processo,
        reu,
        c.oab
        from pastas p,cnpjuf c
        where p.estado=c.uf and p.pasta= %s
    """

    try:
        result=[]
        parametros = cod_pasta
        db_cursor.execute(sql_command,[cod_pasta])
        row = db_cursor.fetchone() 
        result.append(row[0])  #pasta
        result.append(row[1])  #cod_cliente
        result.append(row[2])  #autor
        result.append(row[3])  #comarca
        result.append(row[4])  #estado
        result.append(row[5])  #orgao
        result.append(row[6])  #num_orgao
        result.append(row[7])  #vara
        result.append(row[8])  #cobertura
        result.append(row[9])  #secao
        result.append(row[10]) #nr_processo
        result.append(row[11]) #reu
        result.append(row[12]) #oab

        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")

    return result

def f002_sql(cod_pasta):


    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()

    sql_command =   """
        Select * from view_pecasUtilitarios_01 where pasta = ?
    """
    try:
        db_cursor.execute(sql_command,[cod_pasta])
        row = db_cursor.fetchone() 
        result = {
            "pasta":row[0],
            "codigoSaj":row[1],
            "cod_cliente":row[2],
            "num_orgao":row[3],
            "orgao":row[4],
            "preposicao":row[5],
            "secao":row[6],
            "nr_processo":row[7],
            "valor_inicial":row[8],
            "dat_citacao":row[9],
            "dat_distribuicao":row[10],
            "situacaoSaj":row[11],
            "comarca":row[12],
            "estado":row[13],
            "estadouf":row[14],
            "advConveniado":row[15],
            "oabConveniado":row[16],
            "advExAdverso":row[17],
            "oabExAdverso":row[18],
            "reu":row[19],
            "enderecoReu":row[20],
            "cnpjReu":row[21],
            "coreu":row[22],
            "enderecoCoReu":row[23],
            "cnpjCoReu":row[24],
            "autor":row[25],
            "vitima":row[26],
            "cobertura":row[27],
            "consorcio":row[28],
            "contrato":row[29],
            "merito":row[30],
            "advSupervisor":row[31],
            "oabJbUF":row[32],
            "dataDoAcordo":row[33],
            "valorDoAacordo":row[34],
            "percentualDeSucumbencia":row[35],
            "valorDaParte":row[36],
            "valorHonorariosAdvogado":row[37],
            "representado":row[38],
            "formaDePagamento":row[39],
            "dataReclamacao":row[40],
            "subjudice":row[41],
            "valor_indenizacao":row[42],
            "dataSinistro":row[43],
            "dataSinistroJudicial":row[44],
            "representacao":row[45],
            "dataRegistroBO":row[46],
            "publicando_nome":row[47],
            "publicando_oab":row[48],
            "nr_processoSE":row[49],
            "camara_civel":row[50],
            "juizo":row[51],
            "uf":row[52]
        }
        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")

    return result

def f002_descricao_dano(id_dano):


    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()

    sql_command =   """
        select texto from danoscorporais where id_danocorporal = ?
    """
    try:
        db_cursor.execute(sql_command,[id_dano])
        row = db_cursor.fetchone() 
        retorno=row[0]
        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na consulta")
    return retorno


def view_informacoesDaPasta(cod_pasta):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()

    sql_command =   """
        select * from view_pasta_redator
        where pasta=?
   """

    try:
        db_cursor.execute(sql_command, [cod_pasta])
        row = db_cursor.fetchone()
        dados_da_pasta = {
            'pasta':row[0],
            'cod_cliente':row[1],
            'nr_processo':row[2],
            'comarca':row[3],
            'uf':row[4],
            'juizo':row[5],
            'cobertura':row[6],
            'dat_citacao':row[7],
            'dat_distribuicao':row[8],
            'cliente':row[9],
            'conv_nome':row[10],
            'conv_oab':row[11],
            'publicando_nome':row[12],
            'publicando_oab':row[13],
            'publicando_sexo':row[14],
            'autor':row[15],
            'orgao':row[16],
            'id_pasta':row[17],
            'oabjb': row[18],
            'valorDoPagamento':row[19],
            'nr_processoSE':row[20]
        }

        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")
    return dados_da_pasta



def view_pasta(cod_pasta):
    db_connection = p.connect(stringConnexao.strSqlServer())
    db_cursor = db_connection.cursor()
    retorno=[]

    sql_command =   """
        select * from view_pasta_redator
        where pasta=?
   """

    try:
        db_cursor.execute(sql_command, [cod_pasta])
        row = db_cursor.fetchone()

        retorno.append(row[0])
        retorno.append(row[1])
        retorno.append(row[2])
        retorno.append(row[3])
        retorno.append(row[4])
        retorno.append(row[5])
        retorno.append(row[6])
        retorno.append(row[7])
        retorno.append(row[8])
        retorno.append(row[9])
        retorno.append(row[10])
        retorno.append(row[11])
        retorno.append(row[12])
        retorno.append(row[13])
        retorno.append(row[14])
        retorno.append(row[15])
        retorno.append(row[16])
        retorno.append(row[17])
        retorno.append(row[18])


        db_cursor.close()
        del db_cursor
        db_connection.close()

    except p.IntegrityError:
        print ("Erro na inclusao")
    return retorno

