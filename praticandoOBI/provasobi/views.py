from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Prova, Problema, Questao, Alternativa, ProvaPerson,Classificacao
from .forms import ProvaForm
from django.db.models import Q
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})
    # data = {}
    # data['provas'] = Prova.objects.all()
    # return render(request, 'home.html', data)

def provas(request):
    data = {}
    data['provas'] = Prova.objects.all()
    return render(request, 'provas.html', data)

def problemas(request, pk):
    problemas = Problema.objects.all().select_related('codprova').filter(codprova=pk)
    provas = Prova.objects.filter(codprova=pk)

    id_prob = []
    for p in problemas:
        id_prob.append(p)

    questoes = Questao.objects.all().select_related('codproblema').filter(codproblema__in=id_prob).order_by('numeroquestao')#.filter(codproblema__in=id_questoes)

    id_questoes = []
    for q in questoes:
         id_questoes.append(q)

    alternativas = Alternativa.objects.all().select_related('codquestao').filter(codquestao__in=id_questoes)

    return render(request, 'problemas.html', {'problemas': problemas, 'questoes': questoes, 'alternativas': alternativas, 'provas':provas})
    #data = {}
    #data['problemas'] = Problema.objects.filter(pk=pk)
    #return render(request, 'problemas.html', data)



def busca(request):
    error=False
    if 'q' in request.GET:
        q = request.GET['q']
        checkbox = request.GET.get("display_type", None)
        if not q:
            error=True
        else:
            if q.isnumeric() == False:
                erroinput = True
                return render(request, 'busca/busca_form.html', {'erroinput': erroinput})
            elif checkbox == 'anobox':
                provas = Prova.objects.filter(anoprova=q)
                return render(request, 'busca/busca_resultado.html', {'provas': provas, 'query': q})
            elif checkbox == 'fasebox':
                provas = Prova.objects.filter(faseprova=q)
                return render(request, 'busca/busca_resultado.html', {'provas': provas, 'query': q})
            elif checkbox == 'nivelbox':
                provas = Prova.objects.filter(nivelprova=q)
                return render(request, 'busca/busca_resultado.html', {'provas' : provas, 'query': q})
            else:
                provas = Prova.objects.filter(Q(anoprova=q) | Q(faseprova=q) | Q(nivelprova=q))
                return render(request, 'busca/busca_resultado.html', {'provas' : provas, 'query': q})
        provas = Prova.objects.all()
        return render(request, 'busca/busca_resultado.html', {'provas': provas, 'query': q})
    return render(request, 'busca/busca_form.html', {'error':error})

def buscaprob(request):
    error=False
    if 'q' in request.GET:
        q = request.GET['q']
        checkbox = request.GET.get("display_type", None)
        if not q:
            error=True
        else:
            if checkbox == 'titulobox':
                problemas = Problema.objects.filter(tituloproblema__icontains=q)
                return render(request, 'busca/busca_prob_resultado.html', {'problemas': problemas, 'query': q})
            elif checkbox == 'classificacaobox':
                classificacao = Classificacao.objects.filter(tituloclassificacao__icontains=q)
                problemas = Problema.objects.filter(classificacao__in=classificacao)
                return render(request, 'busca/busca_prob_resultado.html', {'problemas': problemas, 'query': q})
            elif checkbox == 'palavrabox':
                problemas = Problema.objects.filter(Q(tituloproblema__icontains=q) | Q(regrasproblema__icontains=q) | Q(enunciadoproblema__icontains=q))
                return render(request, 'busca/busca_prob_resultado.html', {'problemas': problemas, 'query': q})
            else:
                classificacao = Classificacao.objects.filter(tituloclassificacao__icontains=q)
                problemas = Problema.objects.filter(Q(tituloproblema__icontains=q) | Q(regrasproblema__icontains=q) | Q(enunciadoproblema__icontains=q) | Q(classificacao__in=classificacao))
                return render(request, 'busca/busca_prob_resultado.html', {'problemas': problemas, 'query': q})

        classificacao = Classificacao.objects.all()
        problemas = Problema.objects.all()
        return render(request, 'busca/busca_prob_resultado.html', {'problemas': problemas, 'query': q})
    return render(request, 'busca/busca_prob_form.html', {'error':error})


def problema(request, pk):
    problemas = Problema.objects.all().filter(codproblema=pk)

    id_prob = []
    for p in problemas:
        id_prob.append(p)
        codp = p.codprova.codprova

    provas = Prova.objects.filter(codprova=codp)

    questoes = Questao.objects.all().select_related('codproblema').filter(codproblema__in=problemas).order_by('numeroquestao')#.filter(codproblema__in=id_questoes)

    id_questoes = []
    for q in questoes:
         id_questoes.append(q)

    alternativas = Alternativa.objects.all().select_related('codquestao').filter(codquestao__in=id_questoes)

    return render(request, 'problemas.html', {'problemas': problemas, 'questoes': questoes, 'alternativas' : alternativas, 'provas':provas})