from django.urls import path
from .views import listado_familiares, inicio

urlpatterns = [
    path('', inicio),
    path('listado-familiares/', listado_familiares),
]