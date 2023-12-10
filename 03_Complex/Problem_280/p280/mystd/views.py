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
        new_list = [i for i in lst if not(i.startswith("aa"))]
        print(new_list)
    else:
       form = StudentList()
      
    context = {
        'form':form,
        'new_list':new_list
  
    }
    return render(request, "mystd/home.html",context)