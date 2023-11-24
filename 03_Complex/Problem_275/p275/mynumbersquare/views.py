from django.shortcuts import render
from .forms import UserNumber

def home(request):
    num1_sq = None
    num2_sq = None
    final_result = None
    if request.method == "POST":
        form = UserNumber(request.POST)
        num1 = int(form['num1'].value())
        num2 = int(form['num2'].value())
        num1_sq = num1 * num1
        num2_sq = num2 * num2
        result = num1_sq + num2_sq
        final_result = result * result * result
    else:
        form = UserNumber()
 
    context = {
        'form':form,
        'num1_sq':num1_sq,
        'num2_sq':num2_sq,
        'final_result':final_result

    }
    return render(request, "mynumbersquare/home.html", context)
