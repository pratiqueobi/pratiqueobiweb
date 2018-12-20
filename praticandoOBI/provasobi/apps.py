from django.apps import AppConfig
from watson import search as watson

class ProvasobiConfig(AppConfig):
    name = 'provasobi'

    def ready(self):
        Problema = self.get_model('Problema')
        watson.register(Problema, fields=('tituloproblema',
                                          'enunciadoproblema',
                                          'regrasproblema',
                                          'classificacao'))