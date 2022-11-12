from inspect import ArgSpec
from socket import fromshare
from django import forms
from .models import AllApplicant, Applicant, GradeApplicant,  Profile, Recruiter, Sentiment, EmailUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea 
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


'''class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario_password']'''

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

class AutheticationUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']



class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['profile']

class ApplicantForm(forms.ModelForm):
    class Meta: 
        model = Applicant
        fields = ['university', 'interest', 'lastjob','desclastjob', 'phone']

class RecruiterForm(forms.ModelForm):
    class Meta: 
        model = Recruiter
        fields = ['company', 'phone']

class UpdateApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields= ['university', 'interest', 'lastjob','desclastjob', 'phone']

class GradeApplicantForm(forms.ModelForm):
    class Meta:
        model = GradeApplicant
        fields =['first_name','last_name','relation','soft_skills', 'hard_skills']

class SearchApplicantForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['last_name']

class AllApplicantForm(forms.ModelForm):
    class Meta:
        model = AllApplicant
        fields = []

class SearchApplicantForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name']

class SentimentForm(forms.ModelForm):
    class Meta:
        model = Sentiment
        widgets = {'text_to_analyze': Textarea(attrs= {'cols': 40, 'rows': 5})}
        fields = ['text_to_analyze']


class SendEmailForm(forms.ModelForm):
    class Meta:
        model= EmailUser
        fields=['email_user', 'code']