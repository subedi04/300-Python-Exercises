from multiprocessing import context
from django.shortcuts import render
from . forms import CalForm

def index(request):
    form = None
    answers = None
    if request.method=='POST':
        form = CalForm(request.POST)
        n1 = int(form['n1'].value())
        n2 = int(form['n2'].value())
        add = n1 + n2 
        sub = n1 - n2 
        div = n1 / n2 
        mul = n1 * n2
        answers = [add, sub, div, mul]
    context = {
        'form':CalForm(),
        'answers':answers
    }
    return render(request, "cal/index.html",context)