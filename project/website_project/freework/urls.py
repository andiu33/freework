from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns= [
    path('home', views.home, name= 'home'),
    ##path('createaspirante', views.create_aspirante),
    ##path('createreclutador', views.create_reclutador),
    ##path('updateusuario/<int:usuario_id>', views.update_usuario),
    path('listusuario', views.list_usuario),
    
    
]