import json
from django.db import IntegrityError
import glob
from provasobi.models import *

files = glob.glob("provas/*.json")
for file in files:
    prova = open(file, 'r')
    prova = prova.read()
    prova = json.loads(prova)
    prova_obj, created = Prova.objects.get_or_create(anoprova=prova['anoprova'], nivelprova=prova['nivelprova'],
                                     faseprova=prova['faseprova'])
    if created:
        prova_obj(urlprova=prova['urlprova'])
    prova_obj.save()
    numproblema = 1
    for problema in prova['problemas']:
        try:
            while 1:
                try:
                    Problema.objects.get(codprova=prova_obj, numeroproblema=numproblema)
                    numproblema+=1
                except Problema.DoesNotExist:
                    break
            problema_obj = Problema.objects.create(tituloproblema=problema['tituloproblema'],
                                                   enunciadoproblema=problema['enunciadoproblema'],
                                                   regrasproblema=problema['regrasproblema'],
                                                   imgproblema=problema['imgproblema'], numeroproblema=numproblema,
                                                   codprova=prova_obj)
            problema_obj.classificacao.set(problema['classificacao'])
            problema_obj.save()
            numproblema += 1
            numeroquestao = 1
            for questao in problema['questoes']:
                questao_obj = Questao.objects.create(numeroquestao=numeroquestao,
                                                     enunciadoquestao=questao['enunciadoquestao'],
                                                     gabaritoquestao=questao['gabaritoquestao'],
                                                     imgquestao=questao['imgquestao'],
                                                     codproblema=problema_obj)
                questao_obj.save()
                numeroquestao += 1
                for alt in questao['alternativas']:
                    alt_obj = Alternativa.objects.create(letraalternativa=alt['letraalternativa'],
                                                         textoalternativa=alt['textoalternativa'],
                                                         codquestao=questao_obj)
                    alt_obj.save()
        except IntegrityError:
            print('Problema já existe')

