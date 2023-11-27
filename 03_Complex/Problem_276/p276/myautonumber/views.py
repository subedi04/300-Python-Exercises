from django.shortcuts import render
from .forms import UserNum
def home(request):
    answer = None
    if request.method == "POST":
        form = UserNum(request.POST)
        n1 = int(form['n1'].value())
        half_n1 = n1/2
        answer = n1 + half_n1
        print(answer) 
    else:
        form = UserNum()
 
    context = {
        'form':form,
        'answer':answer
   
    }
    return render(request, "myautonumber/home.html", context)
