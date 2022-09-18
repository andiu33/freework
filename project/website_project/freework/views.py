from cgitb import text
from itertools import count
from urllib.request import Request
from .forms import * 
from .models import *
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 



##from website_project.freework.forms import CreateUsuarioForm, UpdateUsuarioForm
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def reclutador(request):
    return render(request, 'reclutador.html', {})   

'''def create_aspirante(request):
    data_result ={'form_create_usuario': CreateUsuarioForm}
    if request.method =='POST':
        formulario = CreateUsuarioForm(request.POST)
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_result['message'] = "¡Listo! Ahora formas parte de Freework :D"
        else:
            data_result['message'] = "Por favor vuelve a intentarlo :("
    print(data_result)
    return render (request, 'freework/aspirante_create.html', data_result)

def create_reclutador(request):
    data_result ={'form_create_usuario': CreateUsuarioForm}
    if request.method =='POST':
        formulario = CreateUsuarioForm(request.POST)
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_result['message'] = "¡Listo! Ahora formas parte de Freework :D"
        else:
            data_result['message'] = "Por favor vuelve a intentarlo :("
    print(data_result)
    return render (request, 'freework/reclutador_create.html', data_result)'''

@login_required
def list_usuario(request):
    usuarios= Usuario.objects.all()
    data_result ={'usuario_list':usuarios}
    return render (request, 'usuario_list.html', data_result)


'''def update_usuario(request, usuario_id):
    usuarios= Usuario.objects.get(pk=usuario_id)
    formulario =UpdateUsuarioForm()
    data_result={'usuario':usuarios}
    data_result['formulario']=formulario
    
    print(request.POST)
    formulario = UpdateUsuarioForm(request.POST, instance= usuarios)
    print(request.POST)
    if formulario.is_valid():
        formulario.save()
        data_result['message'] = "¡Listo! Actualizado de forma correcta ;)"
    else:
        data_result['message'] = "Por favor vuelve a intentarlo :("
    return render (request, 'usuario_update.html', data_result)'''


'''def login_usuario(request):
    data_result ={'form_login_usuario': LoginUsuarioForm}
    if request.method =='POST':
        formulario = AuthenticationForm(request.POST)
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_result['message'] = "Correcto"
        else:
            data_result['message'] = "Incorrecto :("
    print(data_result)
    return render (request, 'freework/login.html', data_result)'''

def createuser (request):
    user_form = CreateUserForm()
    contexto = {'user_form': user_form}
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    return render(request,'createuser.html',contexto)
