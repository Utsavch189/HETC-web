from calendar import c
import random
from datetime import datetime
import hashlib
from hashlib import blake2b
from hmac import compare_digest
from secrets import token_bytes
from .models import Student


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
                return False
     
     return True