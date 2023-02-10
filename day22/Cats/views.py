from django.shortcuts import render, redirect
from .models import Price     
from .forms import PriceForm
from .ColorsPlus import ColorPlus
from itertools import groupby
from django.db.models import Count
# Create your views here.

def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")

def all_cat(request):
    Cats = Price.objects.all()
    mapper = {"CATS": Cats}
    return render(request,"Cats/allcats.html", mapper)


def catsbycolor(request,color_name):
    
    listcats= Price.objects.filter(color=color_name)
    
    
    
    mapper = {"LISTBYCOLOR": listcats}
    return render(request, "Cats/catsbycolor.html" ,mapper)
    



def all_color(request):
    colors = Price.objects.values("color").distinct()
    catnumber =[]
    for color in colors:
        c = ColorPlus()
        
        c.color = color["color"] # Список цветов
        c.text = "<---Посмотреть--->"
        c.n = Price.objects.filter(color=c.color).count()
        catnumber.append(c)
    
    mapper = {"COLORS": catnumber}
    return render(request,"Cats/allcolors.html", mapper)





def add_cat(request):
    
    if request.method != "POST":
        form = PriceForm()
    else:
        form = PriceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allCats")
    mapper = {"FORM": form}
    return render(request, "Cats/add_Cat.html", mapper)
        
    
