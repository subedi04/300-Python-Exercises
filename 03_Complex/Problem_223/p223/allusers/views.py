from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User 

def home(request):
    users = User.objects.all() 
    context = {
        'users':users
    }
    return render(request, "allusers/home.html",context)