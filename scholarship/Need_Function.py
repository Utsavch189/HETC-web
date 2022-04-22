from calendar import c
import random
from datetime import datetime
import hashlib
from secrets import token_bytes

key = token_bytes(16)

def ID(username):
    a=random.randint(101,999)
    idd=username+str(a)
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




