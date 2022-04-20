from calendar import month
from html.entities import codepoint2name
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
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view








def home(request):
    
    field_name = 'date'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    date = getattr(obj, field_object.attname)

    field_name = 'month'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    month = getattr(obj, field_object.attname)


    field_name = 'start_time'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    time = getattr(obj, field_object.attname)

    field_name = 'exam_duration'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    exam_duration = getattr(obj, field_object.attname)


    field_name = 'total_questions'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    total_questions = getattr(obj, field_object.attname)


    field_name = 'registration_last_date'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    registration_last_date = getattr(obj, field_object.attname)


    field_name = 'registration_last_month'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    registration_last_month = getattr(obj, field_object.attname)


    dictt={
    'exam_date':eliminate( date),
    'exam_month':eliminate( month),
    'exam_start_time':eliminate (time),
    'exam_duration':eliminate(exam_duration),
    'number_of_questions':eliminate(total_questions),
    'registration_last_date':eliminate(registration_last_date),
    'registration_last_month':eliminate(registration_last_month)

}

 
    return render(request,'home.html',{'dictt':dictt})


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
       m=''
       

       if request.method=="GET":
            field_name = 'date'
            obj = DetailsExam.objects.first()
            field_object = DetailsExam._meta.get_field(field_name)
            date = getattr(obj, field_object.attname)

            field_name = 'month'
            obj = DetailsExam.objects.first()
            field_object = DetailsExam._meta.get_field(field_name)
            month = getattr(obj, field_object.attname)


            field_name = 'start_time'
            obj = DetailsExam.objects.first()
            field_object = DetailsExam._meta.get_field(field_name)
            time = getattr(obj, field_object.attname)

            field_name = 'exam_duration'
            obj = DetailsExam.objects.first()
            field_object = DetailsExam._meta.get_field(field_name)
            exam_duration = getattr(obj, field_object.attname)


            field_name = 'total_questions'
            obj = DetailsExam.objects.first()
            field_object = DetailsExam._meta.get_field(field_name)
            total_questions = getattr(obj, field_object.attname)


            dictt={
    'exam_date':eliminate( date),
    'exam_month':eliminate( month),
    'exam_start_time':eliminate (time),
    'exam_duration':eliminate(exam_duration),
    'number_of_questions':eliminate(total_questions),
    

}
            return render(request,'exam.html',{'dictt':dictt})
            
            
       elif request.method=="POST":
            
            
            if ( request.headers['Content-Length']=='14' ):
                
               
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                m = (body['msg'])
                
                print('message',m)

                
               
              
                
               
               

                
                
            else:
                
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                index1 =str( (body['index']))
                option=(body['option'])
                print(' index and option',index1, option)
                
                r_object=(ChoosedOptions.objects.filter(userid=request.user.username))
                if(r_object.exists()):
                    obb=(r_object.filter(questionNumber=index1))
                    if(obb.exists()):
                        obb.delete()
                        x=ChoosedOptions(author=request.user,userid=request.user.username,questionNumber=index1,selectedOption=option)
                        x.save()
                    else:
                         x=ChoosedOptions(author=request.user,userid=request.user.username,questionNumber=index1,selectedOption=option)
                         x.save()

                else:
                    
                   ChoosedOptions.objects.create(author=request.user,userid=request.user.username,questionNumber=index1,selectedOption=option)
                    

               


            
            return render(request,'exam.html')
      
    
    


def notexam(request):
    field_name = 'date'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    date = getattr(obj, field_object.attname)

    field_name = 'month'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    month = getattr(obj, field_object.attname)


    field_name = 'start_time'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    time = getattr(obj, field_object.attname)

    field_name = 'exam_duration'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    exam_duration = getattr(obj, field_object.attname)


    field_name = 'total_questions'
    obj = DetailsExam.objects.first()
    field_object = DetailsExam._meta.get_field(field_name)
    total_questions = getattr(obj, field_object.attname)


    dictt={
    'exam_date':eliminate( date),
    'exam_month':eliminate( month),
    'exam_start_time':eliminate (time),
    'exam_duration':eliminate(exam_duration),
    'number_of_questions':eliminate(total_questions)

}

    return render(request,'notexam.html',{'dictt':dictt})







def loginn(request):
   
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

def Credentials(request):
    if request.method=='GET':
        field_name = 'date'
        obj = DetailsExam.objects.first()
        field_object = DetailsExam._meta.get_field(field_name)
        date = getattr(obj, field_object.attname)

        field_name = 'month'
        obj = DetailsExam.objects.first()
        field_object = DetailsExam._meta.get_field(field_name)
        month = getattr(obj, field_object.attname)


        field_name = 'start_time'
        obj = DetailsExam.objects.first()
        field_object = DetailsExam._meta.get_field(field_name)
        time = getattr(obj, field_object.attname)

       



        if is_exam(date,month,time):
            return render(request,'exam_cred.html')
        else:
            
            return redirect('notexam')

    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if username == request.user.username and user is not None:
            return redirect('exam')
        else:
            messages.warning(request,'Wrong Username or Password')  
            return render(request,'exam_cred.html')   
        


@api_view(['POST','GET'])
def api(request):
    if request.method=='POST':
        index=str(request.data['index'])
        obb=ChoosedOptions.objects.filter(userid=request.user.username)
       
        selected=obb.filter(questionNumber=index).values('selectedOption')

        print(selected[0]['selectedOption'])
        
    
        r_obj=Question.objects.get(pk=index)
        #r_obj1=ChoosedOptions.objects.get(pk=index)
        a={"id":index,"question":r_obj.ques,"opt1":r_obj.opt1,"opt2":r_obj.opt2,"opt3":r_obj.opt3,"opt4":r_obj.opt4,"selectedOption":selected[0]['selectedOption']}
        data=json.dumps(a)

    
        return Response(data)
    elif request.method=='GET':
        r_obj=Question.objects.get(pk=1)
        a={"id":1,"question":r_obj.ques,"opt1":r_obj.opt1,"opt2":r_obj.opt2,"opt3":r_obj.opt3,"opt4":r_obj.opt4}
        data=json.dumps(a)

    
        return Response(data)
