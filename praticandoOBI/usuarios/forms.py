from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from provasobi.models import ProvaPerson

class ProvaForm(forms.ModelForm):
    class Meta:
        model = ProvaPerson
        fields = ('titulo', 'ano', 'dificuldade', 'observacoes',)


class QuestoesForm(forms.ModelForm):
    class Meta:
        model = ProvaPerson
        fields = ('titulo', 'ano', 'dificuldade', 'observacoes',)


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'email',)

class ProfileForm(UserCreationForm):
    data_nascimento = forms.DateField(required=False, help_text='Formato: YYYY-MM-DD')
    localizacao = forms.CharField(required=False, help_text='Estado')
    instituicao = forms.CharField(required=False, help_text='Instituição de Ensino')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'data_nascimento', 'localizacao', 'instituicao', 'password1', 'password2',)

    # @transaction.atomic
    # def save(self, data_nascimento, localizacao, instituicao):
    #     user = super().save(commit=False)
    #     user.save()
    #     Profile.objects.create(user=user)
    #     user.profile.data_nascimento = data_nascimento
    #     user.profile.localizacao = localizacao
    #     user.profile.instituicao = instituicao
    #     user.profile.save()
    #     return user