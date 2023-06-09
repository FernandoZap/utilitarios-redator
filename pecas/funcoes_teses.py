
def f002_teses_embargos_omissao(respostas,teses):
    if respostas['intimacao_mp']=='N':
        teses['IntimacaoDoMP']='S'
    if respostas['cj_peremp_litisp']=='1':
        teses['CoisaJulgada']='S'
    elif respostas['cj_peremp_litisp']=='2':
        teses['Perempcao']='S'
    elif respostas['cj_peremp_litisp']=='3':
        teses['Litispendencia']='S'
    if respostas['prescricao']=='S':
        teses['OmissaoPrescricao']='S'
    if respostas['pagamento_adm']=='N':
        teses['OmissaoPagamentoAdm']='S'
    if respostas['prop_inadimp_com_pagto_Adm']=='N':
        teses['OmissaoInadimplente']='S'
    if respostas['lesao_pre']=='S':
        teses['OmissaoLesaoPreExistente']='S'
    if respostas['omissao_regulacao_8']=='S':
        teses['OmissaoRegulacao8']='S'
    if respostas['juros_citacao']=='2':
        teses['OmissaoDosConsecutariosLegais']='S'
    if respostas['correcao_monetaria']=='2':
        teses['OmissaoDosConsecutariosLegais']='S'

    return teses
