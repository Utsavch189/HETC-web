from calendar import c
import random
from datetime import datetime


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
    c_date=datetime.today().strftime("%d")
    c_month=datetime.today().strftime("%m")
    

    c_hour=datetime.now().strftime("%H")
    c_minute=datetime.now().strftime("%M")
    if(str(c_date)==str(date) and str(c_month)==str(month) and str(c_hour)==str(time) ):
        return True
    else:
        return False
    
a='11'
b='04'
c='12'
print(is_exam(a,b,c))
