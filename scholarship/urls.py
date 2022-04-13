from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name='home'),
   path('contact',contact,name='contact'),
   path('register',register,name='register'),
   path('exam',exam,name='exam'),
   path('notexam',notexam,name='notexam'),
    path('login',loginn,name='login'),
   
]
