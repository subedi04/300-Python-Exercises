from django.shortcuts import render
from .forms import UserForce
def home(request):
    f = None
    if request.method == "POST":
        form = UserForce(request.POST)
        m = float(form['m'].value())
        a = float(form['a'].value())
        f = m * a
        print(f)
    else:
        form = UserForce()
 
    context = {
        'form':form,
        'f':f
 
    }
    return render(request, "manforce/home.html", context)
