from django.shortcuts import render
from .models import Brand, Model, Color, Recording
# Create your views here.

def index(request):
    """Home page of application"""
    return render(request, "Phone/index.html")

def allPhones(request):
    recording = Recording.objects.order_by("date_added")
    mapper = {"RECORDING": recording}
    return render(request, "Phone/recording.html", mapper)


def allBrand(request):
    brand = Recording.objects.values("brand")
    listbrand = []
    for i in brand:
        bunit = Brand.objects.get(id=i["brand"])
        listbrand.append(bunit)
    listbrand = set(listbrand)
    mapper = {"ALLBRAND": listbrand}
    return render(request, "Phone/allbrand.html", mapper )

def choicemodel(request, brand_id):
    r = Recording.objects.filter(brand=brand_id)
    models = []
    for i in r:
        models.append(i.model)
    models = set(models)
    mapper = {"ALLMODELS": models}
    return render(request, "Phone/allmodels.html", mapper )


def model(request, brand, model):
    models= Recording.objects.filter(brand=brand, model=model)
    mapper = {"MODELS": models}
    return render(request, "Phone/models.html", mapper)