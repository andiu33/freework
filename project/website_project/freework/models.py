from email.policy import default
from socket import SIO_KEEPALIVE_VALS
from typing_extensions import Self
from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phone_field import PhoneField

# Create your models here.

'''class Usuario(models.Model):
    usuario_name = models.CharField(max_length = 100)
    usuario_email = models.CharField(max_length = 50)
    usuario_type = models.CharField(max_length = 1)
    usuario_password = models.CharField(max_length = 8)


    def __str__(self):
        return 'Datos del usuario:%s %s %s %s' %(self.usuario_name,self.usuario_email,self.usuario_type, self.usuario_password)


class Aspirante(models.Model):
    ##OnetoOneField

    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    nombre =models.CharField(max_length=255,blank=False,null=False)
    universidad = models.CharField(max_length=255,blank=False,null=False)
    enfoque = models.CharField(max_length=255,blank=False,null=False)
    celular = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return 'Datos del usuario:%s %s %s' %(self.id,self.universidad,self.enfoque)

class Recruiter(models.Model):
    id = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=255,blank=False,null=False)
    phone = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return 'Datos del usuario:%s %s %s' %(self.id,self.empresa,self.celular)
'''
PROFILE_CHOICES =(
        ("Aspirante", "Aspirante"),
        ("Reclutador", "Reclutador")
    )

INTEREST_CHOICES =(
    
    ("Humanidades", "Humanidades"),
    ("Ciencias exactas", "Ciencias exactas"),
    ("Ciencias naturales", "Ciencias naturales"),
    ("Ciencias sociales", "Ciencias sociales"),
    ("Ciencias de la salud", "Ciencias de la salud"),
    ("Negocios", "Negocios"),
    ("Leyes", "Leyes"),
    ("Tecnología", "Tecnologia")
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    profile = models.CharField(max_length=20, choices= PROFILE_CHOICES, default='1', null=True )



    def __str__(self):
        return 'Datos del usuario:%s' %(self.name)

class Recruiter(models.Model):
    user= models.OneToOneField(User, on_delete =models.CASCADE, null =True)
    company = models.CharField(max_length=255,blank=False,null=True)
    phone = models.PositiveIntegerField(blank = True, null = True)
    def __str__(self):
        return 'Datos del usuario:%s' %(self.company)



class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE, null =True)    
    university = models.CharField(max_length=255,blank=False,null=True)
    interest = models.CharField(max_length=20, choices = INTEREST_CHOICES, default= '1', null=True)
    lastjob= models.CharField(max_length=255,blank=False,null=True)
    desclastjob = models.CharField(max_length=255,blank=False,null=True)
    phone = models.PositiveIntegerField(blank = True, null = True)
    
class Sentiment(models.Model):
    text_to_analyze= models.CharField(max_length=255)
    analyze_save = models.CharField(max_length=255)
    def __str__ (self):
            return 'el sentimiento es %s %s' % (self.text_analyzed)

class EmailUser2(models.Model):
    email_user = models.CharField(max_length=100)
    code = models.CharField(max_length = 13, blank =True, null = True)
    user = models.ForeignKey(User, on_delete =models.CASCADE, null =True)
    applicant = models.ForeignKey(Applicant, on_delete =models.CASCADE, null =True)

class GradeApplicant(models.Model):
    sentiment = models.OneToOneField(Sentiment, on_delete =models.CASCADE, null =True) 
    user= models.ForeignKey(User, on_delete =models.CASCADE, null =True)
    first_name =  models.CharField(max_length=255,blank=False,null=True)
    last_name =  models.CharField(max_length=255,blank=False,null=True)
    relation =  models.CharField(max_length=255,blank=False,null=True)
    soft_skills = models.PositiveIntegerField(blank = True, null = True)
    hard_skills = models.PositiveIntegerField(blank = True, null = True)
    applicant = models.ForeignKey(Applicant, on_delete =models.CASCADE, null =True)
    code = models.OneToOneField(EmailUser2,on_delete =models.CASCADE, null =True )
    random = models.CharField(max_length = 13, blank = True, null = True)
    def __str__(self):
        return '%s' %(self.soft_skills)

class MoreJobs(models.Model):
    user= models.ForeignKey(User, on_delete =models.CASCADE, null =True)
    applicant = models.ForeignKey(Applicant, on_delete =models.CASCADE, null =True)
    newjob = models.CharField(max_length = 13, blank = True, null = True)
    descjob = models.CharField(max_length = 13, blank = True, null = True)
    









class AllApplicant(models.Model):
    user= models.ForeignKey(User, on_delete =models.CASCADE, null =True) 
    applicant= models.ForeignKey(Applicant, on_delete =models.CASCADE, null =True)  


        
