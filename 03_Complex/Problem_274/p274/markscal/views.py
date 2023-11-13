from django.shortcuts import render
from .forms import UserMarks

def home(request):
    total = None
    average = None
    if request.method == "POST":
        form = UserMarks(request.POST)
        s1 = int(form['s1'].value())
        s2 = int(form['s2'].value())
        s3 = int(form['s3'].value())
        s4 = int(form['s4'].value())
        s5 = int(form['s5'].value())
        s6 = int(form['s6'].value())
        total = s1+s2+s3+s4+s5+s6
        average = total/6
        
    else:
        form = UserMarks()
 
    context = {
        'form':form,
        'total':total,
        'average':average,
    
    }
    return render(request, "markscal/home.html", context)
