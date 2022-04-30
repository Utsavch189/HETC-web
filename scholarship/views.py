from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .models import *
from django.core.mail import send_mail
from .Need_Function import ID,PASSWORD,is_exam,eliminate,hashed,hashed2,verified,last_seen,is_exam_running
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json






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
def exam(request,pp):
 
       

       if request.method=="GET":
           
            if(is_exam_running(request.user.username)):
                user = request.user
                userid = bytes(pp, 'UTF-8')
                if(verified(user.username,userid)):
                
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
                        'is_exam':is_exam(date,month,time)
                        }
                    return render(request,'exam.html',{'dictt':dictt})
                else:
                
                    return render(request,'exam_cred.html')
            else:
                messages.warning(request,'Your Exam is over')
                return render(request,'exam_cred.html')

       elif request.method=="POST":
            
            
            if ( request.headers['Content-Length']=='14' ):
                
               
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                m = (body['msg'])
                print(m)
                Student.objects.filter(user_id=pp).update(exam_status=m)
                total=0
                
                rr_obj=ChoosedOptions.objects.filter(userid=pp)
                

                qq_obj=Question.objects.all()
                for i in rr_obj:
                    for j in qq_obj:
                        if(j.ques_no==int(i.questionNumber)):
                            if(j.opt_ans==i.selectedOption):
                                total=total+j.marks
                                
                            
                yy=Result(result=total,userid=pp)
                yy.save()


            elif ( request.headers['Content-Length']=='63' ):
                
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                times = (body['msg'])
                
                
                Student.objects.filter(user_id=pp).update(last_seen=last_seen(times))
                

                
               
              
                
               
               

                
                
            else:
                
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                index1 =str( (body['index']))
                option=(body['option'])
                print(' index and option',index1, option)
                
                if(index1!='0'):

                    r_object=(ChoosedOptions.objects.filter(userid=pp))
                    if(r_object.exists()):
                        obb=(r_object.filter(questionNumber=index1))
                        if(obb.exists()):
                            obb.update(selectedOption=option)
                        
                        else:
                            ChoosedOptions.objects.create(author=request.user,userid=pp,questionNumber=index1,selectedOption=option)


                    else:
                    
                        ChoosedOptions.objects.create(author=request.user,userid=pp,questionNumber=index1,selectedOption=option)
                    

               


            
            return render(request,'exam.html')
      
    
    






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
        is_exam_running(request.user.username)
        
        return render(request,'exam_cred.html')
      
       

    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if username == request.user.username and user is not None:
            encoded_username = hashed2(username).decode('UTF-8')
            return redirect(f'exam/{encoded_username}/')
        else:
            messages.warning(request,'Wrong Username or Password')  
            return render(request,'exam_cred.html')   
        


@api_view(['POST','GET'])
def api(request,ps):
    dd=Student.objects.filter(user_id=ps)
    if request.method=='POST':
        index=str(request.data['index'])
        print(index)
        obb=ChoosedOptions.objects.filter(userid=ps)
        
       
        if(obb.exists()):
            selected=obb.filter(questionNumber=index).values('selectedOption')
            r_obj=Question.objects.get(pk=int(index))
            if(selected.exists()):
               

        
        
    
        
        
                a={"id":index,"question":r_obj.ques,"opt1":r_obj.opt1,"opt2":r_obj.opt2,"opt3":r_obj.opt3,"opt4":r_obj.opt4,"selectedOption":selected[0]['selectedOption']}
                data=json.dumps(a)

    
                return Response(data)
            else:
                r_obj=Question.objects.get(pk=int(index))
                a={"id":index,"question":r_obj.ques,"opt1":r_obj.opt1,"opt2":r_obj.opt2,"opt3":r_obj.opt3,"opt4":r_obj.opt4,"selectedOption":'None'}
                data=json.dumps(a)
                return Response(data)

        else:
            r_obj=Question.objects.get(pk=int(index))
            a={"id":index,"question":r_obj.ques,"opt1":r_obj.opt1,"opt2":r_obj.opt2,"opt3":r_obj.opt3,"opt4":r_obj.opt4,"selectedOption":'None'}
            data=json.dumps(a)

    
            return Response(data)

    return Response({'status':200})




#########################################################
#Teacher################################################

def students(request):
    if request.user.is_superuser:
        return render(request,'students.html')
    else:
        messages.warning(request,'You are not admin') 
        return render(request,'login.html')



@api_view(['GET','POST'])
def student(request):
    if request.method=='GET':
        st=[]
        t=[]
        c=0
        for i in User.objects.all(): 
            if(i.username!='hetc' ):     
                st.append(i.username)

        for i in st:
            c+=1
            obb=Student.objects.filter(user_id=i)
            res=Result.objects.filter(userid=i)
            if(res.exists()):
                results=res.values('result')
                y={
                "id":c,
                "userID":i,
                "first_name":obb.values('first_name'),
                "last_name":obb.values('last_name'),
                "date_of_birth":obb.values('date_of_birth'),
                "gurdian_name":obb.values('gurdian_name'),
                "contact":obb.values('contact'),
                "whatsapp":obb.values('whatsapp'),
                "email":obb.values('email'),
                "address":obb.values('address'),
                "institute_name":obb.values('school_college_name'),
                "appearing_passed_12":obb.values('appearing_passed_12'),
                "board_name":obb.values('board_name'),
                "appeared_wbjee_jeeMain":obb.values('appeared_wbjee_jeeMain'),
                "result":results,
            }
            else:
                y={
                "id":c,
                "userID":i,
                "first_name":obb.values('first_name'),
                "last_name":obb.values('last_name'),
                "date_of_birth":obb.values('date_of_birth'),
                "gurdian_name":obb.values('gurdian_name'),
                "contact":obb.values('contact'),
                "whatsapp":obb.values('whatsapp'),
                "email":obb.values('email'),
                "address":obb.values('address'),
                "institute_name":obb.values('school_college_name'),
                "appearing_passed_12":obb.values('appearing_passed_12'),
                "board_name":obb.values('board_name'),
                "appeared_wbjee_jeeMain":obb.values('appeared_wbjee_jeeMain'),
                "result":[ {
                'result':'None'
                }],
            }
    
        
            t.append(y)
        
        return Response(t)
    elif request.method=='POST':

    


        return Response({'status':200})


def SetExamDetails(request):
    if request.method=='POST':
        Edate=request.POST.get('ExamDate')
        Emonth=request.POST.get('ExamMonth')
        EstartTime=request.POST.get('ExamStartTime')
        Edur=request.POST.get('ExamDurationTime')
        TotalQues=request.POST.get('TotalQues')
        RegLastDate=request.POST.get('RegLastDate')
        RegLastMonth=request.POST.get('RegLastMonth')
        DetailsExam.objects.update(date=Edate,month=Emonth,start_time=EstartTime,exam_duration=Edur,total_questions=TotalQues,registration_last_date=RegLastDate,registration_last_month=RegLastMonth)
        messages.success(request,'Successfully Updated')
    return render(request,'SetExam.html')


def SetQuestion(request):
    if request.method=='POST':
        Qnum=request.POST.get('QuesNumber')
        Qbody=request.POST.get('QuesBody')
        opa=request.POST.get('opa')
        opb=request.POST.get('opb')
        opc=request.POST.get('opc')
        opd=request.POST.get('opd')
        currect=request.POST.get('currect')
        marks=request.POST.get('marks')
        y=Question(ques_no=eliminate(Qnum),ques=Qbody,opt1=opa,opt2=opb,opt3=opc,opt4=opd,opt_ans=currect.lower(),marks=eliminate(marks),neg_marks=0)
        y.save()
        messages.success(request,'Successfully Added')
    dictt={
            "total":Question.objects.count()
        }
    
    return render(request,'SetQuestion.html',{'dictt': dictt})


