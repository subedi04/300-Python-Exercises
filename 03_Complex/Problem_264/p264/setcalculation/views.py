from multiprocessing import context
from django.shortcuts import render


def home(request):
    a = {3,2,4,5,6,7,8}
    b  = {4,12,5,1,6,8}
    u = a.union(b)
    i = a.intersection(b)
    context = {
        'u':u,
        'i':i
    }
    return render(request, "setcalculation/home.html", context)