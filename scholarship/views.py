from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')


def register(request):
    return render(request,'register.html')


def Login(request):
    return render(request,'login.html')


def exam(request):
    if User.is_anonymous:
        return redirect('/login')
    return render(request,'exam.html')
