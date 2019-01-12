from provasobi.models import *

for questao in Questao.objects.all():
    alternativas = Alternativa.objects.filter(codquestao=questao)
    texto = ''
    for alternativa in alternativas:
        texto += alternativa.textoalternativa+'|'
        alternativa.delete()
    texto = texto[:-1]
    questao.alternativas = texto
    questao.save()