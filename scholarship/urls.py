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
   path('greet/<st>/',greet),



   path('students/',students,name='students'),
   path('student/',student),
   path('SetExamDetails/',SetExamDetails,name='SetExamDetails'),
   path('SetQuestion/',SetQuestion,name='SetQuestion'),
]
