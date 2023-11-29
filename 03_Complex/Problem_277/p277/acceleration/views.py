from re import T
from django.shortcuts import render
from .forms import FindAcce
def home(request):
    a = None
    if request.method == "POST":
        form = FindAcce(request.POST)
        v = float(form['v'].value())
        t = float(form['t'].value())
        a = v/t
        print(a)
    else:
        form = FindAcce()
 
    context = {
        'form':form,
        'a':a
     
    }
    return render(request, "acceleration/home.html", context)
