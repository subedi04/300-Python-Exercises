from multiprocessing import context
from django.shortcuts import render
from . forms import ListItem

def home(request):
    list_addition = None
    if request.method == "POST":
        form = ListItem(request.POST)
        l1 = int(form["l1"].value())
        l2 = int(form["l2"].value())
        l3 = int(form["l3"].value())
        l4 = int(form["l4"].value())
        l5 = int(form["l5"].value())
        lst = [l1, l2, l3, l4, l5]
        list_addition = 0
        for i in lst:
            if i > 5 and i < 10:
                list_addition += i
    else:   
       form = ListItem()
      
    context = {
        'form':form,
        'list_addition':list_addition
       
    }
    return render(request, "addlistitem/home.html",context)