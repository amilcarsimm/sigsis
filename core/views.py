# -*- coding: UTF8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

from .models import Modulo, Roteiro, Index
from .simulador import *
from django.http.response import HttpResponseRedirect


# Create your views here.
def index(request):
    modulos = Modulo.objects.order_by('mod_seq')
    roteiros = Roteiro.objects.order_by('rot_seq')
    indexs = Index.objects.order_by('index_titulo')
    
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'modulos': modulos, 'roteiros':roteiros, 'indexs':indexs,
        })
    return HttpResponse(template.render(context))


def detalhe(request, mod_id, rot_id):
    
    modulos = Modulo.objects.order_by('mod_seq')
    roteiros = Roteiro.objects.order_by('rot_seq')
    
    modulo = Modulo.objects.get(id=mod_id)
    roteiro = Roteiro.objects.get(id=rot_id)
    simulador = get_simulador(request)
    template = loader.get_template('detalhe.html')
    context = RequestContext(request, {
        'modulo': modulo, 'roteiro':roteiro, 'modulos': modulos, 'roteiros':roteiros, 'simulador':simulador,
        })
    return HttpResponse(template.render(context))
    
def simulador(request):
    
    modulos = Modulo.objects.order_by('mod_seq')
    roteiros = Roteiro.objects.order_by('rot_seq')
    
    simulador = get_simulador(request)
    template = loader.get_template('simulador-somente.html')
    context = RequestContext(request, {
        'modulos': modulos, 'roteiros':roteiros, 'simulador':simulador,
        })
    return HttpResponse(template.render(context))
