from django.shortcuts import render
from .forms import UserName
import cryptocode
def home(request):
    name = None
    encoded_name = None
    if request.method == "POST":
        form = UserName(request.POST)
        name = form['name'].value()
        print(name)
        encoded_name = cryptocode.encrypt(name, "123")
        print(encoded_name)
    else:
        form = UserName()
 
    context = {
        'form':form,
        'name':name,
        'encoded_name':encoded_name,
    }
    return render(request, "nameencrypt/home.html", context)
