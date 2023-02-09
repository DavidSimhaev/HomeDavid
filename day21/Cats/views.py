
from django.shortcuts import render, redirect
from .models import Breed, Temperament, Color, Price
from .forms import TempForm, BreedForm, ColorForm, CatForm
from .Colorplus import ColorPlus



def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


def allbreed(request):
    breedname = Breed.objects.all()
    mapper = {"BREED": breedname }
    return render(request, "Cats/allbreed.html", mapper)


def allTemp(request):
    temps = Temperament.objects.all()
    mapper = {"TEMP": temps }
    return render(request, "Cats/allTemp.html", mapper)

def allColor(request):
    temps = Color.objects.all()
    catsnumbers = []
    for color in temps:
        c = ColorPlus()
        c.color = color
        c.text = "<-Есть в наличии"
        c.n = Price.objects.filter(color=color.id).count()
        if c.n == 0:
            c.n = ""
        catsnumbers.append(c)
    mapper = {"COLORS": catsnumbers}
    return render(request, "Cats/allcolors.html", mapper)



def allcats(request):
    listcats = Price.objects.all()
    mapper = {"CATS": listcats}
    return render(request, "Cats/date_cats.html", mapper)


def catsbycolor(request, color_id):
    listcats = Price.objects.filter(color=color_id)
    mapper = {"LISTBYCOLOR": listcats}
    return render(request, "Cats/filttredcats.html" ,mapper)
    


def statetemperament(request, breed_id):
    b = Price.objects.filter(breed=breed_id)
    temper = []
    mapper = {"TEMPERAMENTS": b}
    return render(request, "Cats/Temp.html", mapper)







def add_breed(request):
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = BreedForm()
    else:
        form = BreedForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allbreed")
    mapper = {"FORMBREED": form}
    return render(request, "Cats/addBreed.html", mapper)
    

def add_temp(request):
    
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = TempForm()
    else:
        form = TempForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allTemp")

    mapper= {"FORM": form}
    return render(request, "Cats/addTemp.html", mapper)


def add_color(request):
    
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = ColorForm()
    else:
        form = ColorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allColor")

    mapper= {"FORM": form}
    return render(request, "Cats/addColor.html", mapper)

def add_cat(request):
    
    if request.method != "POST":
        # NO DATE IN REQUEST
        form = CatForm()
    else:
        form = CatForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cats:allCats")

    mapper= {"FORM": form}
    return render(request, "Cats/addCat.html", mapper)


