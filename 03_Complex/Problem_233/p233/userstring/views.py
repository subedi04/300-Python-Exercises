from multiprocessing import context
from pickle import NONE
from django.shortcuts import render
from . forms import UserString

def home(request):
    user_str_len = None
    sp = None
    user_str_upper = None
    if request.method == "POST":
        form = UserString(request.POST)
        user_str = form['str'].value()
        user_str_upper = user_str.upper()
        user_str_len = len(user_str)
        print(user_str_len)
        sp = 0
        for i in user_str:
            if i.isspace():
                sp += 1
        print(sp)
    else:
        form = UserString()
    
    context = {
        'form':form,
        'user_str_upper':user_str_upper,
        'user_str_len':user_str_len,
        'sp':sp
    }
    return render(request, "userstring/home.html",context)