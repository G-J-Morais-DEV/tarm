from django.contrib import admin
from django.urls import path
from .views import cad_func,listar_func, apagar_func, update_func, escala_func

urlpatterns = [
    path('cadastro/', cad_func, name='cad_func'),
    path('listar_func/',listar_func, name='listar_func'),
    path('listar_func/apagar/<str:nome>', apagar_func, name='apagar_func'),
    path('listar_func/update_func/<str:id>',update_func,name='update_func'),
    path('escala_func',escala_func, name='escala_func'),
]

