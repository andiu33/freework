from socket import fromshare
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


'''class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =['usuario_name','usuario_email','usuario_type', 'usuario_password']



class LoginUsuarioForm(forms.ModelForm):
    class Meta:
        model:Usuario
        fields = ['usuario_email', 'usuario_password']'''


class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario_password']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class AutheticationUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']