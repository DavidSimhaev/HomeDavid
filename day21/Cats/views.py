
from django.shortcuts import render, redirect
from .models import Breed, Temperament, Color, Age, Price
from .forms import TempForm, BreedForm



def index(request):
    """Home page of application"""
    return render(request, "Cats/index.html")


def allbreed(request):
    breed = Price.objects.values("breed")
    listbreed = []
    for i in breed:
        breedunit = Breed.objects.get(id=i["breed"])
        listbreed.append(breedunit)
    listbreed = set(listbreed)
    mapper = {"BREED": listbreed}
    return render(request, "Cats/allbreed.html", mapper)


def statetemperament(request, breed_id):
    b = Price.objects.filter(breed=breed_id)
    temper = []
    for i in b:
        temper.append(i.temperament)
    temper = set(temper)
    mapper = {"TEMPERAMENTS": temper}
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
            return redirect("Cats:statetemperament")

    mapper= {"FORM": form}
    return render(request, "Cats/addTemp.html", mapper)

