import email
from pyexpat import model
from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    date_of_birth=models.CharField(max_length=50)
    gurdian_name=models.CharField(max_length=100)
    contact=models.CharField(max_length=11)
    whatsapp=models.CharField(max_length=11)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    school_college_name=models.CharField(max_length=50)
    appearing_passed_12=models.CharField(max_length=50)
    board_name=models.CharField(max_length=10)
    appeared_wbjee_jeeMain=models.BooleanField(null=True)
    created_at=models.DateField(datetime.now(),null=True)
