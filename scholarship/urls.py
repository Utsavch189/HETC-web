from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name='home'),
   path('contact/',contact,name='contact'),
   path('register/',register,name='register'),
   path('credentials/exam/<pp>/',exam,name='exam'),
   path('login/',loginn,name='login'),
   path('logout/',logoutt,name='logout'),
   path('credentials/',Credentials,name='credentials'),
   path('api/<ps>/',api,name='api'),



   path('teacher/students',students,name='students'),
   path('student/',student),
]
