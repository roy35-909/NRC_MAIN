from __future__ import division
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Guest, News, Project, Team, User,Home,Notice,Faq,Catagory,What_you_get,Sponsor
from django.contrib.auth.models import auth
from django.conf import settings
from django.core.mail import send_mail
def home(request):
    query = Home.objects.get(signature="roy77")
    notices = Notice.objects.all().order_by('-id')[:5]
    faq = Faq.objects.all()
    catagory = Catagory.objects.all()
    what = What_you_get.objects.all()
    news = News.objects.all()
    sponsor = Sponsor.objects.all()
    return render(request,'home.html',{'data':query,'notices':notices,'faqs':faq,'catagorys':catagory,'whats':what,'newss':news,'sponsors':sponsor})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email ,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"User Not found.")
            return redirect('/login')

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'register.html')
    if request.method =='POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exist. Please Login")
            return redirect('/register')
        name = request.POST['name']
        phone = request.POST['phone']
        t_shirt_size = request.POST['size']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password!=cpassword:
            messages.error(request, 'Password Dont match.')
            return redirect('/register')
        else:

            user = User.objects.create_user(email,password)
            user.first_name = name
            user.phone = phone
            user.t_shirt_size = t_shirt_size
            user.save()
            userr = auth.authenticate(email = email ,password = password)
            if userr is not None:
                auth.login(request,userr)
                return redirect("/profile")
            else:
                messages.error(request,"User Not found.")
                return redirect('/login')
import uuid          

def logout(request):
    auth.logout(request)
    return redirect('/')


def fpass(request):
    if request.method=='GET':
        return render(request,'fpass.html')
    if request.method=='POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        
        if user.exists():
            user2 = User.objects.get(email = email)
            user2.fpass_token = str(uuid.uuid4())
            send_mail_with_token(email,user2.fpass_token)
            user2.save()
            return render(request,'reset_password.html',{'userdetails':user2})
        else:
            messages.error(request,"Enter a Email that is in Our Database.")
            return redirect('/fpass')

def send_mail_with_token(email,token):
    subject = "NRC Password Reset Token"
    message = f" Your Token is : {token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print(email)
    send_mail(subject,message,email_from,recipient_list)
def payment_apcepted(email,name):
    subject = "National Robotics Competition(NRC)"
    message = f"Dear, {name},We successfully Receive Your Payment. Check your Profile."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
def email_for_all(list,message):
    subject = "National Robotics Competition(NRC)"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,message,email_from,list)



def reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        token = request.POST['token']
        user = User.objects.get(email=email)
        if user.fpass_token == token:
            user.set_password(password)
            user.save()
            return redirect('/login')
        else:
            messages.error(request,"Token don't match.")
            return redirect('/fpass')

def team_info(request,division):
    if request.user.is_staff:
        if division=="all":
            user = User.objects.filter(is_selected=True)
            return render(request,'show_team_info.html',{'data':user})
        else:
            user = User.objects.filter(is_selected=True,project__distric__contains=division)
            return render(request,'show_team_info.html',{'data':user})
    else:
        return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('/login')

def complete_profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            catagory = Catagory.objects.all()
            return render(request,'complete_profile.html',{'update':request.user.is_team_registration_done,'catagory':catagory})
        else:
            return redirect('/login')
    if request.method =='POST':
        project_titile = request.POST['p_t']
        team_name = request.POST['t_n']
        institute = request.POST['i_n']
        catagory = request.POST['catagory']
        description = request.POST['description']
        
        if request.user.is_team_registration_done:
            u = Project.objects.get(leader = request.user)
            u.project_title = project_titile
            u.team_name = team_name
            u.institution = institute
            u.catagory = catagory
            u.description = description
            u.save()
            return redirect('/profile')
        divi = request.POST['division']
        if request.POST['m_1_n'] and request.POST['m_1_e']:
            t = Team(leader=request.user,name = request.POST['m_1_n'],email=request.POST['m_1_e'],t_shirt_size=request.POST['m_1_s'])
            t.save()
        if request.POST['m_2_n'] and request.POST['m_2_e']:
            t = Team(leader=request.user,name = request.POST['m_2_n'],email=request.POST['m_2_e'],t_shirt_size=request.POST['m_2_s'])
            t.save()
        if request.POST['m_3_n'] and request.POST['m_3_e']:
            t = Team(leader=request.user,name = request.POST['m_3_n'],email=request.POST['m_3_e'],t_shirt_size=request.POST['m_3_s'])
            t.save()
        if request.POST['m_4_n'] and request.POST['m_4_e']:
            t = Team(leader=request.user,name = request.POST['m_4_n'],email=request.POST['m_4_e'],t_shirt_size=request.POST['m_4_s'])
            t.save()
        info = Project(leader = request.user,project_title=project_titile,team_name=team_name,institution=institute,catagory=catagory,description=description,distric=divi)
        info.save()
        q = request.user
        q.is_team_registration_done = True
        q.save()
        return redirect('/profile')

def payment(request):
    if request.method == 'GET':
        triger = Home.objects.get(signature="roy77").open_payment_link
        return render(request,'payment.html',{"triger":triger})
        
    if request.method =='POST':
        email = request.POST['email']
        t_id = request.POST['t_id']
        user = User.objects.filter(email=email)
        if User.objects.filter(payment_id = t_id):
            messages.error(request,"Payment Id Already Exist")
            return redirect('/payment')
        if user.exists():
            user2 = User.objects.get(email=email)
            if (user2.is_payment_done and request.user.is_authenticated==False) or (request.user.is_authenticated and request.user.email != email):
                messages.error(request,"Payment Id Already In Database . For Change : login , Go to Profile , Click makePayment ,Give Id Again")
                return redirect('/login')   
            user2.payment_id=t_id
            user2.is_payment_done=True
            user2.save()
            if request.user.is_authenticated:
                return redirect('/profile')
            else:
                return redirect('/')
        else:
            messages.error(request,"Email Not Found .Please Enter Registered Email.")
            return redirect('/payment')

def a_payment(request):
    if request.method=='GET':
        if request.user.is_superuser:
            query = User.objects.filter(is_payment_done = True,is_payment_apcepted=False)
            return render(request,'transcript.html',{'data':query})
        else:
            return redirect('/login')
def a_payment_done(request,email):
    if request.user.is_superuser:
        user = User.objects.get(email=email)
        user.is_payment_apcepted = True
        user.is_selected = True
        user.save()
        payment_apcepted(email,user.first_name)
        return redirect('/transcript')
    else:
        return redirect('/login')
def delete(request,email):
    if request.user.is_superuser:
        user = User.objects.get(email = email)
        user.is_payment_done = False
        user.save()
        return redirect('/transcript')
    else:
        return redirect('/login')



def about(request):
    query = Home.objects.get(signature="roy77")
    return render(request,'about.html',{"data":query})
def guest(request):
    query = Home.objects.get(signature="roy77")
    i_c_c_g = Guest.objects.filter(inaguration_crermony_chief_guest=True)
    c_c_c_g = Guest.objects.filter(closing_crermony_chief_guest=True)
    h_j = Guest.objects.filter(honorable_judge=True)
    return render(request,'guest.html',{"data":query,"first_guest":i_c_c_g,"secound_guest":c_c_c_g,"h_j":h_j})
def news(request):
    query = Home.objects.get(signature="roy77")
    news = News.objects.all()
    return render(request,'news.html',{"data":query,"news":news})
def program(request):
    query = Home.objects.get(signature="roy77")
    catagory = Catagory.objects.all()
    return render(request,'program.html',{"data":query,"catagory":catagory})

def projects(request):
    query = Home.objects.get(signature="roy77")
    projects = User.objects.filter(is_selected=True)
    return render(request,'Projects.html',{"data":query,"project":projects})