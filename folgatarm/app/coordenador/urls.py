from django.contrib import admin
from django.urls import path
from .views import homecoord,loginCoordenador,logout_view

urlpatterns = [
   path('', homecoord, name='home'),
   path('login/',loginCoordenador, name='login'),
   path('logout_manager/',logout_view,name='logout_manager'),
]
