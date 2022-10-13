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
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.db.models import Prefetch, Avg
from django.db.models import Avg
from itertools import chain




##from website_project.freework.forms import CreateUsuarioForm, UpdateUsuarioForm

# Create your views here.

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
        print(user_form.errors)
        print(profile_form.errors)
        print(applicant_form.errors)
        
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
            applicant_list2 = GradeApplicant.objects.values('user__username', 'user__first_name', 'user__last_name', 'applicant__university', 'applicant__lastjob', 'applicant__desclastjob').annotate(Avg(('soft_skills'))).annotate(Avg(('hard_skills'))).filter(user__first_name__contains = request.POST.get('first_name'))
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
def gradeapplicant (request, id):
    applicant = Applicant.objects.get(id = id)
    user_id= request.user
    user = User.objects.get(username =request.user.username)    
    grade_form = GradeApplicantForm()    
    contexto = {'grade_form': grade_form, 'user': user, 'user_id':user_id, 'applicant': applicant}    
    if request.method== 'POST':
        print(request.POST)
        grade_form = GradeApplicantForm(request.POST)
        if grade_form.is_valid():                                    
            grade_form = grade_form.save()
            grade_form.applicant = applicant
            grade_form.user = user  
            grade_form.save() 

            return redirect ('homeprofile')
        else:
            return redirect ('home')
    return render(request,'gradeapplicant.html',contexto)       
   


'''def delete_product (request, product_id):
    product = Product.objects.get(pk=product_id)
    data_context = {'product':product}
    if request.method == 'POST':
        print (request.POST)
        if 'yes' in request.POST:
            product.deleted_date = timezone.now()
            product.save()
            return redirect('product')
        elif 'no' in request.POST:
            return redirect('product')
    return render(request,'delete_product.html',data_context)'''

'''def update_aspirante(request, aspiranteinfo_id):
    aspiranteinfo = AspiranteInfo.objects.get(pk= aspiranteinfo_id)'''
    



'''def update_pokemon_pokedexx(request,pokemon_id):
    pokemons = Pokemon.objects.get(pk=pokemon_id)
    formulario = EditPokemonForms()
    data_result = {'pokemon':pokemons}
    data_result ['formulario']= formulario
    print(pokemons)

    if request.method == 'POST':
        formulario = EditPokemonForms(request.POST,instance = pokemons)
        print(request.POST)
        if formulario.is_valid():
            formulario.save()
            data_result['message'] = "Pokemon actualizado"
        else:
            data_result['message'] = "Pokemon no actualizado"

    return render (request,'pokedexx/pokedexx_update.html',data_result)'''




