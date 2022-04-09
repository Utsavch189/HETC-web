from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name='home'),
   path('contact',contact,name='contact'),
   path('register',register,name='register'),
   path('login',Login,name='login'),
   path('exam',exam,name='exam')
]
