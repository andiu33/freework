from django.contrib import admin
from django.urls import path 
from . import views
from django.contrib.auth.views import PasswordResetView 


urlpatterns= [
    path('home', views.home, name= 'home'),
   
   
    path('homeprofile', views.homeprofile, name= 'homeprofile' ),
    path('createapplicant', views.createapplicant, name= 'createapplicant' ),
    path('createrecruiter', views.createrecruiter, name= 'createrecruiter' ),
    path('updateapplicant/<int:id>', views.updateapplicant, name= 'updateapplicant' ),
    path('gradeapplicant/<int:id>', views.gradeapplicant, name= 'gradeapplicant' ),
    path('searchapplicant', views.search_applicant, name= 'searchapplicant' ),
    ##path('updateaspirante/<int:updateaspirante_id>',views.update_aspirante, name ='updateaspirante'),   


]