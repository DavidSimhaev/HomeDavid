from django.shortcuts import render, redirect
from .models import Price, Image
from .forms import PriceForm, ResumeForm, ImageForm
from .ColorsPlus import ColorPlus
from .urlsPlus import urlsPlus
from .catwithimage import CatWithImage
from django.contrib.auth.decorators import login_required
from itertools import groupby
from django.db.models import Count
from django.http import HttpResponseRedirect

# Create your views here.


 



def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")

@login_required
def all_cat(request):    
    Imagesbycat = []
    cats_images = Image.objects.filter(owner=request.user)
    for image in cats_images:
        cwi = CatWithImage()          
        cwi.cat = Price.objects.filter(owner=request.user).get(id=image.id)
        cwi.image = "/media/"+image.image.path
        Imagesbycat.append(cwi)
    
    mapper = {"images": Imagesbycat}
    return render(request,"Cats/allcats.html", mapper)

@login_required
def catsbycolor(request, color_name):
    catsbycolors= Price.objects.filter(owner=request.user,color=color_name)
    cat =[]
    
    for cats in catsbycolors:
        lc = urlsPlus()
        lc.filterby = cats
        lc.cats_id = Image.objects.filter(owner=request.user).get(id=cats.id)
        lc.images="/media/"+lc.cats_id.image.path
        cat.append(lc)
    
    
    mapper = {"LISTBYCOLOR": cat}
    return render(request, "Cats/catsbycolor.html" ,mapper)
    
    

    
@login_required    
def all_color(request):
    colors = Price.objects.values("color").distinct()
    catnumber =[]
    for color in colors:
        c = ColorPlus()
        
        c.color = color["color"] # Список цветов
        c.text = "<---Посмотреть--->"
        c.n = Price.objects.filter(owner=request.user,color=c.color).count()
        c.notext =""
        c.zero = 0
        catnumber.append(c)
    
    mapper = {"COLORS": catnumber}
    return render(request,"Cats/allcolors.html", mapper)


@login_required
def add_cat(request):
    
    if request.method != "POST":
        catform = PriceForm()
        imageform = ImageForm()
    else:
        catform = PriceForm(request.POST)
        imageform = ImageForm(request.POST, request.FILES)
        
        if catform.is_valid() and imageform.is_valid()  :
            cat = catform.save(commit=False)
            cat.owner = request.user
            cat.save()
            image = imageform.save(commit=False)
            image.owner = request.user
            image.save()
            
            catform.save()
            imageform.save()
            return redirect("Cats:allCats")
    mapper = {"catform": catform, "imageform": imageform}
    return render(request, "Cats/add_Cat.html", mapper)
        


        

