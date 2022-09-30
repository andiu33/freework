from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView 


urlpatterns= [
    path('home', views.home, name= 'home'),
    ##path('createaspirante', views.create_aspirante),
    ##path('createreclutador', views.create_reclutador),
    ##path('updateusuario/<int:user_id>', views.update_aspirante),
    ##path('listusuario', views.list_usuario),
    path('createtype/<int:user_id>',views.type_user, name ='createtype'), 
  
    ##path('reset_password/', auth_view.PasswordResetView.as_view(), name= 'password_reset'),
    ##path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    ##path('reset/<uib64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    ##path('reset_password_commplete/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    path('createtype',views.type_user, name ='createtype'),   
    path('applicant',views.applicant, name ='applicant'),   
    path('recruiter',views.recruiter, name ='recruiter'),   
    path('profile', views.profile, name= 'profile'),
    path('inicio', views.inicio, name= 'inicio'),
    path('aspiranteinfo', views.aspiranteinfo, name ='aspiranteinfo'),
    path('homeprofile', views.homeprofile, name= 'homeprofile' ),
    path('createapplicant', views.createapplicant, name= 'createapplicant' ),
    path('createrecruiter', views.createrecruiter, name= 'createrecruiter' ),
    path('updateapplicant/<int:id>', views.updateapplicant, name= 'updateapplicant' ),
    path('gradeapplicant', views.gradeapplicant, name= 'gradeapplicant' ),
    path('infoapplicant', views.infoapplicant, name= 'infoapplicant' ),
    ##path('updateaspirante/<int:updateaspirante_id>',views.update_aspirante, name ='updateaspirante'),   


]