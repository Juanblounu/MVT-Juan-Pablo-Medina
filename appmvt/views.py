from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def listado_familiares(request):
    
    template = loader.get_template('listado_familiares.html')
    
    render = template.render({})
    
    return HttpResponse(render)
