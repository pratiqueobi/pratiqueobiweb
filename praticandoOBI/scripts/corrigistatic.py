from provasobi.models import *

for problema in Problema.objects.all():
    if 'static/' in problema.imgproblema:
        print('problema.imgproblema')
        print(problema.imgproblema.split('static/')[1])