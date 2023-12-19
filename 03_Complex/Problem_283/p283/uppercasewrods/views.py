from multiprocessing import context
from django.shortcuts import render
from . forms import WordsList

def home(request):
    new_list = None
    if request.method == "POST":
        form = WordsList(request.POST)
        w1 = form["w1"].value()
        w2 = form["w2"].value()
        w3 = form["w3"].value()
        w4 = form["w4"].value()
        w5 = form["w5"].value()
        lst = [w1,w2,w3,w4,w5]
        new_list = [i for i in lst if i.isupper()]
    else:
       form = WordsList()
      
    context = {
        'form':form,
        'new_list':new_list
    }
    return render(request, "uppercasewords/home.html",context)