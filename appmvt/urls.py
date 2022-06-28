from django.urls import path
from .views import listado_familiares

urlpatterns = [
    path('', listado_familiares),
]