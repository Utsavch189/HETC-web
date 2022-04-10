from venv import create
from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import *
from django.core.mail import send_mail
from .userid import ID
from django.contrib.auth.decorators import login_required
import random


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')


def register(request):
    

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gurdian=request.POST.get('gurdian')
        year=request.POST.get('year')
        month=request.POST.get('month')
        date=request.POST.get('date')
        phone=request.POST.get('phone')
        whatsapp=request.POST.get('whatsapp')
        email=request.POST.get('email')
        address=request.POST.get('address')
        status=request.POST.get('status')
        board=request.POST.get('board')
        entrance=request.POST.get('entrance')
        instu=request.POST.get('inst')
    
        date_of_birth1=str(date)+'/'+str(month)+'/'+str(year)
        date_of_birth2=str(date)+str(month)+str(year)
        smodel=Student(first_name=fname,last_name=lname,date_of_birth=date_of_birth1,gurdian_name=gurdian,contact=phone,whatsapp=whatsapp,email=email,address=address,school_college_name=instu,appearing_passed_12=status,board_name=board,appeared_wbjee_jeeMain=entrance,created_at=datetime.now())
        smodel.save()

        a=random.randint(199,12999)
        userid=fname+str(a)
        
        subject='Thank You for registration'
        body=f'your user name is {userid} and your password is {date_of_birth2}'
        send_mail(
    subject,
    body,
    'utsavpokemon9000chatterjee@gmail.com',
    [email],
    fail_silently=False,
)
    
        user = User.objects.create_user(userid, email, date_of_birth2)
        user.save()
    
    return render(request,'register.html')


def Login(request):
   if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'exam.html')
        else:
            return render(request,'login.html')

@login_required(login_url='login')
def exam(request):
    if User.is_anonymous:
        return render(request,'login.html')
    return render(request,'exam.html')
