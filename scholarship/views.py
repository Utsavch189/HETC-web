from venv import create
from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import *
from django.core.mail import send_mail
from .Need_Function import ID,PASSWORD,is_exam,eliminate
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

dictt={}



def home(request):
 
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')


def register(request):
    if request.method=="GET":
        return render(request,'register.html')
    

    elif request.method=='POST':
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
        userid=ID(fname)
        password=PASSWORD(date,month,year)
        smodel=Student(first_name=fname,last_name=lname,user_id=userid,date_of_birth=date_of_birth1,gurdian_name=gurdian,contact=phone,whatsapp=whatsapp,email=email,address=address,school_college_name=instu,appearing_passed_12=status,board_name=board,appeared_wbjee_jeeMain=entrance,created_at=datetime.now())
        smodel.save()

        messages.success(request,'Your Registration is completed. Check Your Email To get User ID and Password')
        
        
        subject='Thank You for registration'
        body=f'your user name is {userid} and your password is {password}'
        send_mail(
    subject,
    body,
    'utsavpokemon9000chatterjee@gmail.com',
    [email],
    fail_silently=False,
)
    
        user = User.objects.create_user(userid, email, password)
        user.first_name=fname
        user.last_name=lname
        user.save()

    
    return render(request,'register.html')

@csrf_exempt
@login_required(login_url='login')
def exam(request):
       if request.method=="GET":
            
            return render(request,'exam.html',{'aa':3})
       elif request.method=="POST":
            print(request.body)

            return render(request,'exam.html')
      
    
    


def notexam(request):
   if request.method=="GET":
            
        return render(request,'notexam.html',{'aa':3})
   elif request.method=="POST":
       print(request.body)

       return render(request,'notexam.html')







def loginn(request):
    global dictt
    if request.method=="GET":
        return render(request,'login.html')
   
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:

            login(request,user)

            return redirect('home')
        
        
    messages.warning(request,'Wrong Username or Password')   
    return render(request,'login.html')   

def logoutt(request):
    logout(request)
    return redirect('home')