from django.shortcuts import render,redirect
from django.http import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime


def Home(request):
    return render(request,'Base.html')
