from asyncio.windows_events import NULL
import email
from logging import exception
from logging.config import valid_ident
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
# Create your views here

def index(request):
    return render(request,'index.html')
def myadmin_login(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        print(username)
        print(password)
        messages.success(request, 'Profile details updated.')
        if username=='Akhi' and password=='Akhi':
            return render(request,'index.html')
        else :
            return render(request,'myadmin_login.html')
    return render(request,'myadmin_login.html')
def SupportersLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=Supporter.objects.filter(email=username).filter(password=password)
        request.session['username']=username
        print(request.session['username'])
        if  user.exists():
            print("Success")
            return redirect('/supphome')
        else:
            print("Invalid")
            print(user)
            return render(request,'SupportersLogin.html')
    return render(request,'SupportersLogin.html')
def UsersLogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=my_users.objects.filter(email=username).filter(password=password)
        #print(user)
        request.session['username']=username
        print(request.session['username'])
        if user.exists():
            print("Success")
            return redirect('/userhome')
        else:
            print("Invalid")
            print(user)
            return render(request,'usersLogin.html')
       
    return render(request,'usersLogin.html')
def usersignup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        type="user"
        password=request.POST.get('pwd')
        desc=request.POST.get('desc')
        gforms=request.POST.get('gforms')
        wlink=request.POST.get('wlink')
        donation_done=request.POST.get('donation_done')
        donation_required=request.POST.get('donation_required')
        myuse= my_users(name=name,
                        email=email,
                        phone=phone,
                        type=type,
                        password=password,
                        desc=desc,
                        gforms=gforms,
                        wlink=wlink,
                        donation_required=donation_required,
        )
        try:
            myuse.save()
            return render(request,'usersLogin.html')
        except:
            return render(request,'usersignup.html')
    return render(request,'usersignup.html')
def supsignup(request):
    error=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        type="supporter"
        password=request.POST.get('pwd')
        supporter= Supporter(name=name,email=email,phone=phone,type=type,password=password)
        try:
         supporter.save()
         return render(request,'SupportersLogin.html')
        except:
         return render(request,'supsignup.html')
    return render(request,'supsignup.html')

def userhome(request):
    all_users=my_users.objects.all()
    #print(all_users)
    namer2=request.session.get('username')
    print(namer2)
    return render(request,'userhome.html',{'all_users': all_users,'namer2':namer2})

def supphome(request):
    all_users=my_users.objects.all()
    #print(all_users)
    #print(request.user)
    namer=request.session.get('username')
    print(namer)
    return render(request,'supphome.html',{'all_users': all_users,'namer':namer})
