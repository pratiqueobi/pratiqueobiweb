from django.contrib import admin
from .models import Prova, Classificacao, ProvaPerson, Questao, Problema, Alternativa

import nested_admin


# Customization Admin
class AlternativaInline(nested_admin.NestedTabularInline):
    model = Alternativa
    sortable_field_name = "letraalternativa"
    extra = 0
    max_num = 5

class QuestaoInline(nested_admin.NestedStackedInline):
    model = Questao
    sortable_field_name = "numeroquestao"
    extra = 0
    inlines = [AlternativaInline]

class ProblemaInline(nested_admin.NestedStackedInline):
    model = Problema
    sortable_field_name = "numeroproblema"
    inlines = [QuestaoInline]
    extra = 0


class ProvaAdmin(nested_admin.NestedModelAdmin):
    fields = [('anoprova', 'nivelprova', 'faseprova', 'urlprova')]
    list_display = ['codprova', 'anoprova', 'nivelprova', 'faseprova']
    search_fields = ['nivelprova', 'faseprova', 'anoprova']
    inlines = [ProblemaInline]


class ProvaPersonAdmin(admin.ModelAdmin):
    fields = ['autor', 'titulo', 'ano', 'dificuldade', 'observacoes']
    list_display = ['autor', 'titulo', 'ano']
    search_fields = ['autor', 'ano']


class ClassificacaoAdmin(admin.ModelAdmin):
    fields = [('tituloclassificacao')]
    list_display = ['tituloclassificacao']


class AlternativaAdmin(admin.ModelAdmin):
    fields = [('letraalternativa', 'textoalternativa', 'codquestao')]
    list_display = ['codalternativa', 'letraalternativa']


class QuestaoAdmin(admin.ModelAdmin):
    fields = [('numeroquestao', 'enunciadoquestao', 'imgquestao', 'gabaritoquestao', 'codproblema')]
    list_display = ['numeroquestao', 'codproblema']


class ProblemaAdmin(admin.ModelAdmin):
    fields = [
        ('numeroproblema', 'tituloproblema', 'enunciadoproblema', 'regrasproblema', 'imgproblema', 'classificacao')]
    list_display = ['codproblema', 'numeroproblema', 'tituloproblema']


admin.site.register(Prova, ProvaAdmin)
admin.site.register(Problema, ProblemaAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Alternativa, AlternativaAdmin)
admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(ProvaPerson, ProvaPersonAdmin)

admin.site.site_header = "Praticando OBI"
admin.site.site_title = "Praticando OBI"
