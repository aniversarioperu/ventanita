# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.
from django.shortcuts import render


def index(request):
    return render(request, 'demo/index.html')


def candidatos_con_sentencias(request):
    return render(request, 'demo/1400_candidatos.html')

def las_20_agrupaciones(request):
    return render(request, 'demo/20_agrupaciones.html')
