from django import forms
from .models import ProvaPerson, Questao


class ProvaForm(forms.ModelForm):
    class Meta:
        model = ProvaPerson
        fields = ('titulo', 'ano', 'observacoes',)


class QuestaoForm(forms.ModelForm):
    a = forms.CharField(label='A', widget=forms.Textarea())
    b = forms.CharField(label='B', widget=forms.Textarea())
    c = forms.CharField(label='C', widget=forms.Textarea())
    d = forms.CharField(label='D', widget=forms.Textarea())
    e = forms.CharField(label='E', widget=forms.Textarea())

    class Meta:
        model = Questao
        exclude = ['alternativas']

    def __init__(self, *args, **kwargs):
        super(QuestaoForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance', False):
            alternativas = kwargs['instance'].alternativas.split('|')
            self.fields['a'].initial = alternativas[0]
            self.fields['b'].initial = alternativas[1]
            self.fields['c'].initial = alternativas[2]
            self.fields['d'].initial = alternativas[3]
            self.fields['e'].initial = alternativas[4]

    def save(self, commit=True):
        m = super(QuestaoForm, self).save(commit=False)
        self.instance.alternativas = self.cleaned_data['a'] + '|' + self.cleaned_data['b'] + '|' + \
                                     self.cleaned_data['c'] + '|' + self.cleaned_data['d'] + '|' + \
                                     self.cleaned_data['e']
        if commit:
            m.save()
        return m
