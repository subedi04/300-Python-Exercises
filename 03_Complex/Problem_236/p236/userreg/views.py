from turtle import isvisible
from django.shortcuts import render, redirect
from . forms import UserRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegister()
    
    context = {
       'form':form 
    }

    return render(request, "userreg/register.html", context)

def userlogin(request):
    if request.method == "POST":
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        print(upass)
        print(uname)
        login(request, user)
        return redirect('home')        
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'userreg/login.html',context)

def home(request):
    return render(request, 'userreg/home.html')

def userlogout(request):
    logout(request)
    return redirect('login')
