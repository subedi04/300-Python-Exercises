from django.shortcuts import render
from . forms import Userage

def home(request):
    msg = None
    if request.method == "POST":
        form  = Userage(request.POST)
        age = int(form['age'].value())
        print(age)
        if age == 18 or age > 18:
            msg = "Youa are eligible for voting"
        else: 
            msg = "You are not eligible after "+str(18-age)+ "year, you will be.."
    else:
        form  = Userage()
    context = {
        'form':form,
        'msg':msg
    }
    return render(request, "userage/home.html", context)