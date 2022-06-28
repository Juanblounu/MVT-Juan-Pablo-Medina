from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from appmvt.models import Familiar


def inicio(request):
    return HttpResponse('Primera vista del projecto')

    


def listado_familiares(request):
    
    template = loader.get_template('listado_familiares.html')
    
    familiar = Familiar(nombre = 'Juan', edad = 16)   
    familiar.save()
    
    lista_familiares = Familiar.objects.all()
    
    render = template.render({'lista_familiares': lista_familiares})
    
    return HttpResponse(render)
