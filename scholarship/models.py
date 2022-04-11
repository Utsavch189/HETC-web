import email
from email.policy import default
from pyexpat import model
from turtle import up
from django.db import models
from datetime import datetime

from numpy import mod
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    user_id=models.CharField(max_length=100,blank=True,null=True)
    date_of_birth=models.CharField(max_length=50,blank=True,null=True)
    gurdian_name=models.CharField(max_length=100,blank=True,null=True)
    contact=models.CharField(max_length=11,blank=True,null=True)
    whatsapp=models.CharField(max_length=11,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    school_college_name=models.CharField(max_length=50,blank=True,null=True)
    appearing_passed_12=models.CharField(max_length=50,blank=True,null=True)
    board_name=models.CharField(max_length=10,blank=True,null=True)
    appeared_wbjee_jeeMain=models.CharField(null=True,blank=True,max_length=10)
    created_at=models.DateField()

    def __str__(self):
        return str(self.first_name)+''+str(self.last_name)


class DetailsExam(models.Model):
    date=models.CharField(null=True,blank=True,max_length=5)
    month=models.CharField(null=True,blank=True,max_length=5)
    start_time=models.CharField(null=True,blank=True,max_length=5)
    exam_duration=models.CharField(null=True,blank=True,max_length=5)
    total_questions=models.CharField(null=True,blank=True,max_length=5)



class Rule(models.Model):
    pdf=models.FileField()