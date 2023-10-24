from multiprocessing import context
from django.shortcuts import render
from . forms import AreaofCircle
def home(request):
    area = None
    if request.method=="POST":
        form = AreaofCircle(request.POST)
        r = int(form['r'].value())
        print(r)
        pi = 3.14
        area = pi*r*r

    else:
        form = AreaofCircle()
    
    context = {
        'form':form,
        'area':area
    }
   
    return render(request, "findarea/home.html",context)