from django.shortcuts import render

from std_info.models import StdInfo
from . forms import StdForm

def index(request):
    if request.method == "POST":
        form = StdForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StdForm()
    students = StdInfo.objects.all()

    context = {
        'form':form,
        'students':students,
    }
    return render(request, "std_info/index.html",context)