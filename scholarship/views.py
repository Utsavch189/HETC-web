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
        userid=ID(fname)
        subject='Thank You for registration'
        body=f'your user id is {userid} and your password is {date_of_birth2}'
        send_mail(
    subject,
    body,
    'utsavpokemon9000chatterjee@gmail.com',
    [email],
    fail_silently=False,
)
    return render(request,'register.html')


def Login(request):
    return render(request,'login.html')


def exam(request):
    if User.is_anonymous:
        return redirect('/login')
    return render(request,'exam.html')
