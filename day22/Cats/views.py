from django.shortcuts import render, redirect
from .models import Price, Image
from .forms import PriceForm, ResumeForm, ImageForm
from .ColorsPlus import ColorPlus
from .urlsPlus import urlsPlus

from itertools import groupby
from django.db.models import Count
from django.http import HttpResponseRedirect

# Create your views here.






def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


def all_cat(request):
    
    
    
    
    Imagesbycat = []


    
    
    if request.method == 'GET':
        images = Image.objects.order_by('title')
        cats_id = Image.objects.values('title')
        for id_cat in cats_id:
            c = urlsPlus()
            c.cats_id = Price.objects.filter(id=id_cat["title"]) 
            Imagesbycat.append(c)
            
             
        for images_id in images:
            c = urlsPlus()
            c.image_id = images_id
            Imagesbycat.append(c)   
           
  
     
    
    
    mapper = {"images": Imagesbycat}
    return render(request,"Cats/allcats.html", mapper)


def catsbycolor(request, color_name):
    catsbycolors= Price.objects.filter(color=color_name)
    cat =[]
    
    for cats in catsbycolors:
        lc = urlsPlus()
        lc.filterby = cats
        lc.text = "Добавить картинку"
        cat.append(lc)
    if request.method == 'GET':
        image =  Image.objects.filter(id=7)
        
    
    
    mapper = {"LISTBYCOLOR": cat, "images": image}
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
        form = PriceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Cats:allCats")
    mapper = {"FORM": form}
    return render(request, "Cats/add_Cat.html", mapper)
        


