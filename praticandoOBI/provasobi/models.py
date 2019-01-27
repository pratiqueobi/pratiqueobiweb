from django.db import models
from usuarios.models import Profile
from django.core.validators import MinValueValidator


class Alternativa(models.Model):
    codalternativa = models.AutoField(db_column='codAlternativa', primary_key=True)  # Field name made lowercase.
    letraalternativa = models.CharField(db_column='letraAlternativa', max_length=10, blank=True,
                                        null=True)  # Field name made lowercase.
    textoalternativa = models.TextField(db_column='textoAlternativa', blank=True,
                                        null=True)  # Field name made lowercase.
    codquestao = models.ForeignKey('Questao', models.CASCADE, db_column='codQuestao', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'alternativa'
        ordering = ['letraalternativa']

    def __str__(self):
        return self.letraalternativa


class Prova(models.Model):
    codprova = models.AutoField(db_column='codProva', primary_key=True)  # Field name made lowercase.
    anoprova = models.IntegerField(db_column='anoProva', blank=True, null=True)  # Field name made lowercase.
    nivelprova = models.IntegerField(db_column='nivelProva', blank=True, null=True)  # Field name made lowercase.
    faseprova = models.IntegerField(db_column='faseProva', blank=True, null=True)  # Field name made lowercase.
    urlprova = models.URLField(db_column='urlProva', unique=True, null=True, blank=True,
                               default='https://olimpiada.ic.unicamp.br/passadas/')
    urlgabarito = models.URLField(db_column='urlGabarito', unique=True, null=True, blank=True)

    class Meta:
        unique_together = ['anoprova', 'faseprova', 'nivelprova']
        managed = True
        db_table = 'prova'
        ordering = ['anoprova']

    def __str__(self):
        return str(self.anoprova) + '/nivel' + str(self.nivelprova) + '/fase' + str(self.faseprova)


class Problema(models.Model):
    codproblema = models.AutoField(db_column='codProblema', primary_key=True)
    numeroproblema = models.PositiveIntegerField(db_column='numeroProblema',
                                                 validators=[MinValueValidator(1)])
    tituloproblema = models.TextField(db_column='tituloProblema', blank=True, null=True)
    enunciadoproblema = models.TextField(db_column='enunciadoProblema', blank=True, null=True)
    regrasproblema = models.TextField(db_column='regrasProblema', blank=True, null=True)
    imgproblema = models.TextField(db_column='imgProblema', blank=True, null=True, default='')
    codprova = models.ForeignKey('Prova', models.CASCADE, db_column='codProva', blank=True, null=True)
    classificacao = models.ManyToManyField('Classificacao', blank=True)

    def recorte(self, filename):
        return 'problema/' + str(self.codprova.codprova) + '.' + filename.split('.')[-1]

    image = models.ImageField('Recorte', upload_to=recorte, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'problema'
        unique_together = ['codprova', 'tituloproblema']

    def __str__(self):
        return self.tituloproblema


class Questao(models.Model):
    codquestao = models.AutoField(db_column='codQuestao', primary_key=True)  # Field name made lowercase.
    numeroquestao = models.PositiveIntegerField(db_column='numeroQuestao',
                                                validators=[MinValueValidator(1)])  # Field name made lowercase.
    enunciadoquestao = models.TextField(db_column='enunciadoQuestao', blank=True,
                                        null=True)  # Field name made lowercase.
    alternativas = models.TextField('Alternativas', null=True, blank=True)

    gabaritoquestao = models.CharField(db_column='gabaritoQuestao', max_length=10, blank=True, null=True)
    imgquestao = models.CharField(db_column='imgQuestao', max_length=300, blank=True, null=True, default='')
    codproblema = models.ForeignKey(Problema, models.CASCADE, db_column='codProblema', blank=True, null=True,
                                    related_name="cod_problemas_questao")
    explicativo = models.TextField('Explicação', null=True, blank=True)

    def gabarito(self, filename):
        return 'gabarito/' + str(self.codquestao.codproblema.codprova.codprova) + str(
            self.codquestao.codproblema.numeroproblema) + str(self.codquestao.numeroquestao) + '.' + \
               filename.split('.')[-1]

    explicativo_imagem = models.ImageField('Imagem Explicativa ', null=True, blank=True)

    def recorte(self, filename):
        return 'questao/' + str(self.codproblema.codproblema) + '.' + filename.split('.')[-1]

    image = models.ImageField('Recorte', upload_to=recorte, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'questao'
        verbose_name_plural = 'Questões'
        verbose_name = 'Questão'
        unique_together = ['codproblema', 'numeroquestao']

    def __str__(self):
        return self.numeroquestao.__str__()

    def get_alternativas(self):
        data = []
        letras = ['A', 'B', 'C', 'D', 'E']
        i = 0
        alternativas = self.alternativas.split('|')
        for alternativa in alternativas:
            data.append({'letraalternativa': letras[i], 'textoalternativa': alternativas[i]})
            i += 1
        return data

# class Gabarito(models.Model):
#     codquestao = models.OneToOneField('Questao', models.DO_NOTHING,
#                                       db_column='codQuestao')  # Field name made lowercase.
#     texto = models.TextField('Explicação', null=True)
#
#     def gabarito(self, filename):
#         return 'gabarito/' + str(self.codquestao.codproblema.codprova.codprova) + str(
#             self.codquestao.codproblema.numeroproblema) + str(self.codquestao.numeroquestao) + '.' + \
#                filename.split('.')[-1]
#
#     imagem = models.ImageField('Imagem Explicativa ', null=True)
#
#     def __str__(self):
#         return self.codquestao.codproblema.tituloproblema + str(self.codquestao.numeroquestao)


class Classificacao(models.Model):
    codclassificacao = models.AutoField(db_column='codClassificacao', primary_key=True)
    tituloclassificacao = models.TextField(db_column='tituloClassificacao', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'classificacao'
        verbose_name_plural = 'Classificações'
        verbose_name = 'Classificação'

    def __str__(self):
        return self.tituloclassificacao


class ProvaPerson(models.Model):
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    codprovaperson = models.IntegerField(db_column='codProvaPerson', null=True, default='0')
    titulo = models.TextField(db_column='titulo', blank=True, null=True, default='')
    ano = models.CharField(db_column='ano', max_length=20, blank=True, null=True, default='')
    dificuldade = models.IntegerField(db_column='dificuldade', blank=True, null=True, default=0)
    observacoes = models.TextField(db_column='observacoes', blank=True, null=True, default='')
    questoes = models.ManyToManyField(Questao, blank='True')

    def __str__(self):
        return self.autor.user.username

    class Meta:
        verbose_name_plural = 'Provas personalizadas'
        verbose_name = 'Prova personalizada'
