from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView


urlpatterns= [
    path('home', views.home, name= 'home'),
    ##path('createaspirante', views.create_aspirante),
    ##path('createreclutador', views.create_reclutador),
    ##path('updateusuario/<int:user_id>', views.update_aspirante),
    path('listusuario', views.list_usuario),
    path('createtype/<int:user_id>',views.type_user, name ='createtype'),   
    ##path('reset_password/', auth_views.PasswordResetView.as_view(), name= 'password_reset'),
    ##path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    ##path('reset/<uib64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    ##path('reset_password_commplete/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    path('reclutador/', views.reclutador),
    path('createtype/<int:user_id/',views.type_user, name ='createtype'),   
    path('aspirante/<int:user_id/',views.aspirante, name ='aspirante'),   
    path('reclutador/<int:user_id/',views.reclutador, name ='reclutador'),   
    
]