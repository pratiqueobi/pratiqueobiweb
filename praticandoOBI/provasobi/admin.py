from django.contrib import admin
from .models import Prova, Classificacao, ProvaPerson, Questao, Problema, Alternativa
import nested_admin


# Customization Admin
class AlternativaInline(nested_admin.NestedStackedInline):
    model = Alternativa
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
    list_display = ['codprova', 'anoprova', 'nivelprova', 'faseprova']
    search_fields = ['nivelprova', 'faseprova', 'anoprova']
    list_filter = ['anoprova', 'faseprova', 'nivelprova']
    inlines = [ProblemaInline]


class ProvaPersonAdmin(admin.ModelAdmin):
    list_display = ['autor', 'titulo', 'ano']
    search_fields = ['autor', 'ano']
    list_filter = ['ano', 'dificuldade']


class ClassificacaoAdmin(admin.ModelAdmin):
    list_display = ['tituloclassificacao']


class AlternativaAdmin(admin.ModelAdmin):
    list_display = ['codalternativa', 'letraalternativa']


class QuestaoAdmin(admin.ModelAdmin):
    list_display = ['numeroquestao', 'codproblema', 'image', 'explicativo']


class ProblemaAdmin(admin.ModelAdmin):
    list_display = ['codproblema', 'numeroproblema', 'tituloproblema', 'image']


admin.site.register(Prova, ProvaAdmin)
admin.site.register(Problema, ProblemaAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(Alternativa, AlternativaAdmin)
admin.site.register(Classificacao, ClassificacaoAdmin)
admin.site.register(ProvaPerson, ProvaPersonAdmin)
admin.site.site_header = "Praticando OBI"
admin.site.site_title = "Praticando OBI"
