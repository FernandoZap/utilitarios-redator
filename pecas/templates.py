# -*- coding: utf-8 -*-

from docxtpl import DocxTemplate


def template_peca(context):
    doc = DocxTemplate("C:/temporarios/Template_Modelo.docx")

    

    doc.render(context)

    doc.save("C:/temporarios/template_peca.docx")



def embargosOmissao(context):
    doc = DocxTemplate("C:/TemplatesPecas/Template_EmbargosOmissao.docx")

    nome_da_peca = context['cod_cliente'] + "_Embargos_Omissao.docx"    

    doc.render(context)

    doc.save("C:/PecasElaboradas/"+nome_da_peca)

    return nome_da_peca



def embargosUltrapetida(context):
    doc = DocxTemplate("C:/TemplatesPecas/Template_EmbargosUltrapetita.docx")

    nome_da_peca = context['cod_cliente'] + "_Embargos_Ultrapetita.docx"    

    doc.render(context)

    doc.save("C:/PecasElaboradas/"+nome_da_peca)

    return nome_da_peca


