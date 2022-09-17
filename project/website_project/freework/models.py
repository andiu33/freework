from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
##from django.contrib.auth.forms import User

# Create your models here.

class Usuario(models.Model):
    usuario_name = models.CharField(max_length = 100)
    usuario_email = models.CharField(max_length = 50)
    usuario_type = models.CharField(max_length = 1)
    usuario_password = models.CharField(max_length = 8)


    def __str__(self):
        return 'Datos del usuario:%s %s %s %s' %(self.usuario_name,self.usuario_email,self.usuario_type, self.usuario_password)




