from multiprocessing import context
from django.shortcuts import render
from . forms import AuthorBooks

def home(request):
    authors_dict = None
    if request.method == "POST":
        form = AuthorBooks(request.POST)
        auth1 = form["auth1"].value()
        book1 = form["book1"].value()
        auth2 = form["auth2"].value()
        book2 = form["book2"].value()       
        auth3 = form["auth3"].value()
        book3 = form["book3"].value()   

        dict = {auth1:book1, auth2:book2, auth3:book3}
        authors_dict = dict.items()
    else:
       form = AuthorBooks()
      
    context = {
        'form':form,
        'authors_dict':authors_dict
  
    }
    return render(request, "myauthors/home.html",context)