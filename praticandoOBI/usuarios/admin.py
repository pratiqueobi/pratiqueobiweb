from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = [('user', 'localizacao', 'instituicao', 'data_nascimento')]
    list_display = ['user', 'localizacao', 'instituicao']

# Register your models here.
admin.site.register(Profile, ProfileAdmin)