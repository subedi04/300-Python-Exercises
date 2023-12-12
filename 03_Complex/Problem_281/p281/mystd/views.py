from multiprocessing import context
from django.shortcuts import render
from . forms import StudentList

def home(request):
    if request.method == "POST":
        form = StudentList(request.POST)
        std1 = form["std1"].value()
        std2 = form["std2"].value()
        std3 = form["std3"].value()
        std4 = form["std4"].value()
        std5 = form["std5"].value()
        lst = [std1, std2, std3, std4, std5]
        lst.sort()
        final_list = []
        for i in lst:
            if len(i) == 5:
                final_list.append(i)
        print(final_list)
    else:
       form = StudentList()
      
    context = {
        'form':form,
        'final_list':final_list
  
    }
    return render(request, "mystd/home.html",context)