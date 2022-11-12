from cgitb import text
from itertools import count
from pickle import FALSE
from urllib.request import Request
from .forms import * 
from .models import *
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.db.models import Prefetch, Avg
from django.db.models import Avg
from itertools import chain
import requests, uuid, json
import string
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import requests, uuid




##from website_project.freework.forms import CreateUsuarioForm, UpdateUsuarioForm

# Create your views here.
def error_404(request,exception):
    return render(request,'404.html',{})

def home(request):
    return render(request, 'home.html', {})



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

'''@login_required
def list_usuario(request):
    usuarios= Usuario.objects.all()
    data_result ={'usuario_list':usuarios}
    return render (request, 'usuario_list.html', data_result)'''





def createuser (request):
    user_form = CreateUserForm()
    profile_form = ProfileForm()
    contexto = {'user_form': user_form}
    contexto = {'user_form': user_form, 'profile_form': profile_form}
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():            
            user = user_form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()          
            return redirect ('createtype')
        else:
            return redirect ('login')
    return render(request,'createuser.html',contexto)


def type_user (request):    
    if request.method == 'POST':
        print (request.POST)
        if 'reclutador' in request.POST:            
            return redirect('recruiter')
        elif 'aspirante' in request.POST:
            return redirect('applicant')
    return render(request,'createtype.html')



def aspiranteinfo(request):
    return render(request, 'aspiranteinfo.html', {})

def createapplicant (request):
    profile = Profile.objects
    user_form = CreateUserForm()
    profile_form = ProfileForm()
    applicant_form = ApplicantForm()    
    contexto = {'user_form': user_form, 'profile_form': profile_form, 'applicant_form': applicant_form, 'profile': profile}
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        applicant_form = ApplicantForm(request.POST)
        
        
        if user_form.is_valid() and profile_form.is_valid() and applicant_form.is_valid():                        
            user = user_form.save()
            profile = profile_form.save()
            applicant = applicant_form.save()
            applicant.user = user  
            profile.profile = 'Aspirante'           
            profile.user = user
            profile.save() 
            applicant.save()         
            return redirect ('login')
        else:
            print(user_form.errors)
            print(profile_form.errors)
            print(applicant_form.errors)
            return redirect ('createapplicant')
    return render(request,'createapplicant.html',contexto)    

def createrecruiter (request):
    profile = Profile.objects
    user_form = CreateUserForm()
    profile_form = ProfileForm()
    recruiter_form = RecruiterForm()    
    contexto = {'user_form': user_form, 'profile_form': profile_form, 'recruiter_form': recruiter_form, 'profile': profile}
    if request.method== 'POST':
        print(request.POST)
        user_form = CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        recruiter_form = RecruiterForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() and recruiter_form.is_valid():                        
            user = user_form.save()
            profile = profile_form.save()
            recruiter = recruiter_form.save()
            recruiter.user = user  
            profile.profile = 'Reclutador'           
            profile.user = user
            profile.save() 
            recruiter.save()  
                   
            return redirect ('login')
        else:
            print(user_form.errors)
            print(profile_form.errors)
            print(recruiter_form.errors)           
            return redirect ('createrecruiter')
    return render(request,'createrecruiter.html',contexto)    

def applicant (request):
    applicant_list= Applicant.objects.all()
    data_context = {'applicant_list':applicant_list}
    applicant_form = ApplicantForm()
    data_context['applicant_form'] = applicant_form
    if request.method == 'POST':
        print("entre en post")
        applicant_form = ApplicantForm(request.POST)
        if applicant_form.is_valid():
            applicant_form.save()
            return redirect('login')
    return render(request,'applicantform.html',data_context)

def recruiter (request):
    recruiter_list= Recruiter.objects.all()
    data_context = {'recruiter_list':recruiter_list}
    recruiter_form = RecruiterForm()
    data_context['recruiterr_form'] = recruiter_form
    if request.method == 'POST':
        print("entre en post")
        recruiter_form = RecruiterForm(request.POST)
        if recruiter_form.is_valid():
            profile.profile = "Recruiter"
            recruiter_form.save()
            return redirect('login')
    return render(request,'recruiterform.html',data_context)

def profile (request):
    profile_list = Profile.objects.get()
    data_context ={'profile_list':profile_list}
    perfil_form = ProfileForm()
    data_context['profile_form'] = perfil_form
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('createtype')
    return render(request, 'profileform.html', data_context)


def inicio(request):
    return render(request, 'inicio.html', {})



@login_required
def homeprofile (request):
    user = request.user
    searchapplicantform= SearchApplicantForm()
    applicant= Applicant.objects.all() 
    ##applicant_list2= GradeApplicant.objects.values('user__username', 'user__first_name', 'user__last_name', 'applicant__university', 'applicant__lastjob', 'applicant__desclastjob').annotate(Avg(('soft_skills'))).annotate(Avg(('hard_skills')))        
    
    applicant_list = Applicant.objects.filter(user_id= user)
    user_list =User.objects.all()    
    user_request = User.objects.get(username =request.user.username)
    user_profile =Profile.objects.get(user= user_request)    
    contexto = {'user_data': user_request, 'user_profile': user_profile, 'applicant_list':applicant_list, 'user_list':user_list, 'applicant': applicant,  'searchapplicantform':searchapplicantform}
    ##contexto['applicant_list2']= applicant_list2
    contexto['empty_search'] = True
    if request.method == 'POST':
        searchapplicantform = SearchApplicantForm(request.POST)
        if searchapplicantform.is_valid():
            applicant_list2 = Applicant.objects.values('user__username', 'user__first_name', 'user__last_name', 'university', 'lastjob', 'desclastjob', 'id').filter(user__first_name__contains = request.POST.get('first_name'))
            ##applicant_list2 = GradeApplicant.objects.values('user__username', 'user__first_name', 'user__last_name', 'applicant__university', 'applicant__lastjob', 'applicant__desclastjob', 'id').annotate(Avg(('soft_skills'))).annotate(Avg(('hard_skills'))).filter(user__first_name__contains = request.POST.get('first_name'))
            contexto['applicant_list2'] = applicant_list2
            contexto['empty_search'] = False
    return render(request, 'homeprofile.html', contexto)

@login_required  
def search_applicant (request):
    searchapplicantform= SearchApplicantForm() 
    contexto = {'searchapplicantform': searchapplicantform}
    contexto['empty_search'] = True
    if request.method == 'POST':
        searchapplicantform = SearchApplicantForm(request.POST)
        if searchapplicantform.is_valid():
            applicant_list2 = GradeApplicant.objects.values('user__username', 'user__first_name', 'user__last_name', 'applicant__university', 'applicant__lastjob', 'applicant__desclastjob').annotate(Avg(('soft_skills'))).annotate(Avg(('hard_skills'))).filter(user__first_name__contains = request.POST.get('first_name'))
            contexto['applicant_list2'] = applicant_list2
            contexto['empty_search'] = False
    
    return render(request,'searchapplicant.html',contexto)


@login_required
def updateapplicant(request, id):
    applicant = Applicant.objects.get(id=id)

    if request.method == 'POST':
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('homeprofile')
    else:
        form = ApplicantForm(instance=applicant)

    return render(request,
                'updateapplicant.html',
                {'form': form})
@login_required
def uniqueapplicant (request, applicant_id):
    user = User.objects.all()
    sentiment = Sentiment.objects.all()
    applicant = Applicant.objects.get(pk = applicant_id) 
    gradeapplicant = GradeApplicant.objects.get(pk = applicant_id)
    
    applicant_list = Applicant.objects.values('user__username', 'user__first_name', 'user__last_name','user__email', 'phone' ,'lastjob','desclastjob', 'university').filter(id = applicant_id)
    gradeapplicant_list = GradeApplicant.objects.values('first_name','soft_skills', 'hard_skills', 'sentiment__analyze_save', 'sentiment__text_to_analyze').filter(applicant__id = applicant_id)
    gradeavg= GradeApplicant.objects.values('user__username').annotate(Avg(('soft_skills'))).annotate(Avg(('hard_skills'))).filter(applicant__id = applicant_id)         
    contexto = {'applicant':applicant, 'user': user, 'gradeapplicant': gradeapplicant, 'sentiment': sentiment}
    contexto['applicant_list'] = applicant_list
    contexto['gradeapplicant_list'] = gradeapplicant_list
    contexto['gradeavg'] = gradeavg
    return render(request,'uniqueapplicant.html',contexto) 

@login_required
def gradeapplicant (request, id):
    applicant = Applicant.objects.get(id = id)
    user_id= request.user
    user = User.objects.get(username =request.user.username)    
    grade_form = GradeApplicantForm() 
    sentimentform = SentimentForm()
    sentiment = Sentiment.objects
    contexto = {'grade_form': grade_form, 'user': user, 'user_id':user_id, 'applicant': applicant, 'sentimentform':sentimentform, 'sentiment': sentiment}    
    if request.method== 'POST':
        grade_form = GradeApplicantForm(request.POST)
        sentimentform = SentimentForm(request.POST)
        print(request.POST)
        print(request.POST.get('text_to_analyze'))
        # Add your key and endpoint
        credential = AzureKeyCredential("8b347822bb32465693ae44970d70ea81")
        endpoint = "https://dsccognitivefreework.cognitiveservices.azure.com/"

        text_analytics_client= TextAnalyticsClient(endpoint,credential)
        documents= [
            request.POST.get('text_to_analyze')
        ]

        response = text_analytics_client.analyze_sentiment(documents, language = "es")
        result = [doc for doc in response if not doc.is_error]
        print(result)
        
        for doc in result:
            print(f"Overrall sentiment: {doc.sentiment}")
            print(
                f"Scores:positive ={doc.confidence_scores.positive};"
                f"neutral={doc.confidence_scores.neutral};"
                f"negative={doc.confidence_scores.negative}\n;"
            )
        sentiment = sentimentform.save()
        sentiment.analyze_save = doc.sentiment
        sentiment.save()
        sentimentform = sentimentform.save()
        contexto['sentimentresult'] = doc.sentiment
        if grade_form.is_valid():                                    
            grade_form = grade_form.save()
            grade_form.applicant = applicant
            grade_form.user = user  
            grade_form.sentiment = sentiment
            grade_form.save() 

            return redirect ('homeprofile')
        else:
            return redirect ('home')
    return render(request,'gradeapplicant.html',contexto)       
    
@login_required
def comment_detail (request, sentiment_id):
    gradeapplicant = GradeApplicant.objects.get(pk=sentiment_id)
    comment_detail_list = GradeApplicant.objects.values('sentiment__text_to_analyze').filter(pk = sentiment_id)
    comment_detail_list2 = Sentiment.objects.values('text_to_analyze').filter(pk =sentiment_id)
    context= {'gradeapplicant': gradeapplicant}
    context['comment_detail_list'] = comment_detail_list
    context['comment_detail_list2'] = comment_detail_list2

    return render(request,'comment.html',context) 



def sentiment (request):
    sentimentform = SentimentForm()
    sentiment = Sentiment.objects
    context = {'sentimentform':sentimentform, 'sentiment': sentiment}

    if request.method == 'POST':

        sentimentform = SentimentForm(request.POST)
        
        print(request.POST)
        print(request.POST.get('text_to_analyze'))
        # Add your key and endpoint
        credential = AzureKeyCredential("8b347822bb32465693ae44970d70ea81")
        endpoint = "https://dsccognitivefreework.cognitiveservices.azure.com/"

        text_analytics_client= TextAnalyticsClient(endpoint,credential)
        documents= [
            request.POST.get('text_to_analyze')
        ]

        response = text_analytics_client.analyze_sentiment(documents, language = "es")
        result = [doc for doc in response if not doc.is_error]
        print(result)
        
        for doc in result:
            print(f"Overrall sentiment: {doc.sentiment}")
            print(
                f"Scores:positive ={doc.confidence_scores.positive};"
                f"neutral={doc.confidence_scores.neutral};"
                f"negative={doc.confidence_scores.negative}\n;"
            )
        sentiment = sentimentform.save()
        sentiment.analyze_save = doc.sentiment
        sentiment.save()
        sentimentform = sentimentform.save()
        context['sentimentresult'] = doc.sentiment
        
    return render(request,'sentiment.html',context)

    
def loggedhome(request):
    return render(request, 'loggedhome.html', {})


def emails(request):
    emailform = SendEmailForm()
    context = {'emailform': emailform}    
    if request.method == 'POST':
        print(request.POST.get('email_user'))
        number_of_strings = 1
        length_of_string = 12
        for x in range(number_of_strings):
            code= (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
        context2 = {'email_user':request.POST.get('email_user'), 'code': code}
        email_to_send = request.POST.get('email_user')
        
        template = get_template('emailtemplate.html')
        content = template.render(context2)
        
        email = EmailMultiAlternatives(
            'FREEWORK',
            'Califica a tu compañer@',
            settings.EMAIL_HOST_USER,
            [email_to_send],
        )        
        email.attach_alternative(content,'text/html')
        email.send()
        #return render(request, 'mail.html',context)        
    return render(request, 'mail.html',context)

def validatecode(request):
    return render(request, 'validatecode.html', {})
