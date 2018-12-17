from django import forms
from .models import ProvaPerson

class ProvaForm(forms.ModelForm):
    class Meta:
        model = ProvaPerson
        fields = ('titulo', 'ano', 'observacoes',)


