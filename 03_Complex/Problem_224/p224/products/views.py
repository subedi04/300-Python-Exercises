from multiprocessing import context
from django.shortcuts import render
from . forms import Productsform

def home(request):
    form = None
    total = None
    net_total = None
    per = None
    if request.method == "POST":
        form = Productsform(request.POST)
        p1 = int(form["p1"].value())
        p2 = int(form["p2"].value())
        p3 = int(form["p3"].value())
        p4 = int(form["p4"].value())
        p5 = int(form["p5"].value())
        p6 = int(form["p6"].value())
        p7 = int(form["p7"].value())
        p8 = int(form["p8"].value())
        p9 = int(form["p9"].value())
        p10 = int(form["p10"].value())

        total = p1 + p2 + p3 + p4 + p5 +p6 + p7 + p8 +p9 + p10
        # 5%
        per = (total / 100) * 5
        net_total = total - per

    else:
       form = Productsform()
      
    context = {
        'form':form,
        'total':total,
        'per':per,
        'net_total':net_total
    }
    return render(request, "products/home.html",context)