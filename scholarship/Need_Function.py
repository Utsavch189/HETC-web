from calendar import c
import random
from datetime import datetime
import hashlib
from hashlib import blake2b
from hmac import compare_digest
from secrets import token_bytes
from .models import *
from django.contrib.auth.models import User
import json
import xlsxwriter

key = token_bytes(16)

def ID(username):
    a=random.randint(101,999)
    idd=username.upper()+str(a)
    return idd

def PASSWORD(date,month,year):
    d=str(date)
    m=str(month)
    y=str(year)
    if len(d)==1 :
        
        if len(m)==1:
            d='0'+d
            m='0'+m
            return d+m+y
            
        else:
            d='0'+d
            return d+m+y

    elif len(m)==1 :
        
        if len(d)==1:
            d='0'+d
            m='0'+m
            return d+m+y
            
        else:
            m='0'+m
            return d+m+y
    else:

        return d+m+y


def is_exam(date,month,time):
    c_date=eliminate( datetime.today().strftime("%d"))
    c_month=eliminate( datetime.today().strftime("%m"))
    

    c_hour=datetime.now().strftime("%H")
    c_minute=datetime.now().strftime("%M")
    if(str(eliminate( c_date))==str(eliminate(date)) and str(eliminate( c_month))==str(eliminate(month)) and str(eliminate( c_hour))==str(eliminate( time)) ):
        return True
    else:
        return True



def eliminate(a):
    a=str(a)
    if(a=='01' or a=='02' or a=='03' or a=='04' or a=='05' or a=='06' or a=='07' or a=='08' or a=='09'):
        n=a.replace('0','')
        return int(n)
    return int(a)


def hashed(a):
    hashed_string = hashlib.sha256(a.encode('utf-8')).hexdigest()
    return hashed_string



def hashed2(string):
    string = bytes(string, 'UTF-8')
    hash = hashlib.blake2b(digest_size=16, key=string)
    hash.update(string)
    return hash.hexdigest().encode('UTF-8')

def verified(string, hashed_string):
    string = hashed2(string)
    return compare_digest(string, hashed_string)


def last_seen(string):
    c_hour=datetime.now().strftime("%H")
    c_minute=datetime.now().strftime("%M")
    return str(c_hour) + ':' +str(c_minute)

def is_exam_running(userid):
     c_hour=eliminate( datetime.now().strftime("%H"))
     c_minute=eliminate( datetime.now().strftime("%M"))
     if(Student.objects.filter(user_id=userid).exists()):
        lSeen=Student.objects.filter(user_id=userid).values('last_seen')[0]['last_seen']
        if lSeen:
            last_hour=eliminate(lSeen[:2])
            last_min=eliminate(lSeen[3:])
     
            if(c_hour==last_hour and c_minute-last_min>15):
                Student.objects.filter(user_id=userid).update(exam_status=True)
            elif(c_hour!=last_hour):
                Student.objects.filter(user_id=userid).update(exam_status=True)
            if(Student.objects.filter(user_id=userid).values('exam_status')[0]['exam_status']==True):
                return True
     
     return True


def excell(msg):
    if msg=='Go':
        st=[]
        t=[]
        
        for i in User.objects.all(): 
            if(i.username!='hetc' ):     
                st.append(i.username)

        for i in st:
         
            obb=Student.objects.filter(user_id=i)
            res=Result.objects.filter(userid=i)
            if(res.exists()):
                results=res.values('result')
                y={
                
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




        workbook=xlsxwriter.Workbook("students.xlsx")
        worksheet=workbook.add_worksheet("firstSheet")
        worksheet.write(0,0,"#")
        worksheet.write(0,1,"UserId")
        worksheet.write(0,2,"FirstName")
        worksheet.write(0,3,"LastName")
        worksheet.write(0,4,"DOB")
        worksheet.write(0,5,"Gurdian")
        worksheet.write(0,6,"Contact")
        worksheet.write(0,7,"WhatsApp")
        worksheet.write(0,8,"Email")
        worksheet.write(0,9,"Address")
        worksheet.write(0,10,"Institute_name")
        worksheet.write(0,11,"appearing_passed_12")
        worksheet.write(0,12,"board_name")
        worksheet.write(0,13,"appeared_wbjee_jeeMain")
        worksheet.write(0,14,"result")

        for i,e in enumerate(t):
          worksheet.write(i+1,0,str(i))
          worksheet.write(i+1,0,e['userID'])  
          worksheet.write(i+1,0,e['first_name'][0]['first_name'])
          worksheet.write(i+1,0,e['last_name'][0]['last_name'])
          worksheet.write(i+1,0,e['gurdian_name'][0]['gurdian_name'])
          worksheet.write(i+1,0,e['date_of_birth'][0]['date_of_birth'])
          worksheet.write(i+1,0,e['contact'][0]['contact'])
          worksheet.write(i+1,0,e['whatsapp'][0]['whatsapp'])
          worksheet.write(i+1,0,e['email'][0]['email'])
          worksheet.write(i+1,0,e['address'][0]['address'])
          worksheet.write(i+1,0,e['institute_name'][0]['school_college_name'])
          worksheet.write(i+1,0,e['appearing_passed_12'][0]['appearing_passed_12'])
          worksheet.write(i+1,0,e['board_name'][0]['board_name'])
          worksheet.write(i+1,0,e['appeared_wbjee_jeeMain'][0]['appeared_wbjee_jeeMain'])
          worksheet.write(i+1,0,e['result'][0]['result'])
        workbook.close()

       





