from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

'''class Usuario(models.Model):
    usuario_name = models.CharField(max_length = 100)
    usuario_email = models.CharField(max_length = 50)
    usuario_type = models.CharField(max_length = 1)
    usuario_password = models.CharField(max_length = 8)


    def __str__(self):
        return 'Datos del usuario:%s %s %s %s' %(self.usuario_name,self.usuario_email,self.usuario_type, self.usuario_password)
'''

class Aspirante(models.Model):
    ##OnetoOneField

    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    nombre =models.CharField(max_length=255,blank=False,null=False)
    universidad = models.CharField(max_length=255,blank=False,null=False)
    enfoque = models.CharField(max_length=255,blank=False,null=False)
    celular = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return 'Datos del usuario:%s %s %s' %(self.id,self.universidad,self.enfoque)

class Reclutador(models.Model):
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    empresa = models.CharField(max_length=255,blank=False,null=False)
    celular = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return 'Datos del usuario:%s %s %s' %(self.id,self.empresa,self.celular)

PERFIL_CHOICES =(
        ("Aspirante", "Aspirante"),
        ("Reclutador", "Reclutador")
    )

ENFOQUE_CHOICES =(
    
    ("Humanidades", "Humanidades"),
    ("Ciencias exactas", "Ciencias exactas"),
    ("Ciencias naturales", "Ciencias naturales"),
    ("Ciencias sociales", "Ciencias sociales"),
    ("Ciencias de la salud", "Ciencias de la salud"),
    ("Negocios", "Negocios"),
    ("Leyes", "Leyes"),
    ("Tecnología", "Tecnologia")
)

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    perfil = models.CharField(max_length=20, choices= PERFIL_CHOICES, default='1' )
    intereses = models.CharField(max_length=20, choices= ENFOQUE_CHOICES, default='8' )

class AspiranteInfo(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE, null =True)
    name = models.CharField(max_length=255,blank=False,null=False)
    last_name = models.CharField(max_length=255,blank=False,null=False)
    universidad = models.CharField(max_length=255,blank=False,null=False)
    ultimotrabajo= models.CharField(max_length=255,blank=False,null=False)
    descultimotrabajo = models.CharField(max_length=255,blank=False,null=False)
    def __str__(self):
        return 'Datos del usuario:%s' %(self.name)
