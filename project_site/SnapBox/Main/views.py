from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from .models import Camera, lens, lightings, tripods, Binoculars
from django.db import connection
from .superclass import Contener
from Cart.forms import CartAddProductsForm
from Cart.Cart import Cart


# Create your views here.
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

CONTENT_FLAG = False

    
def authentication(request):
    __login = request.GET.get('login')
    __password = request.GET.get('password')
    user = authenticate(request, username=__login, password=__password)
    if user is not None:
        login(request, user)
        
        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
    else:
        global CONTENT_FLAG
        CONTENT_FLAG = True
        index = 0
        print(request.META['HTTP_REFERER'])
        #http://127.0.0.1:8000/Lightings/
        l=[]
        print(request.META['HTTP_REFERER'])
        for x in request.META['HTTP_REFERER'][::-1]:
            index +=1
            if index == 1:
                continue
            try:
                int(x)
                break
            except:
                pass
            if x == "/":
                break
            l.extend(x)
        print(l)
        html_name= "".join(l[::-1])
        print(html_name)
        if html_name == "":
            html_name= "Main"
        return redirect(f"Main:{html_name}")


def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))


def Main(request):
    return render(request, "Main/URLS/Main.html")


def Camers(request):
    
    product = Camera.objects.all()
    
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    
    
    
    
    
    
    content = {"Camers":product, "line": 426* line}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Camers.html", content )
    

"""def PR_CAMERS(request, id):
    product = get_object_or_404(Camera, id=id, available = True)
    
    if product.stock < 21:
        pquant = product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    quant = Cart(request).productq(str(id))
    
    return render(request, 
                  "Shope/product/detail.html",{
                      "ProductS": product,
                      "quant": quant ,
                      "cart_product_form":cart_product_form})
    
    
"""    

    
    
    
    
    
def Lens(request):
    product = lens.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    
    print(request.META['HTTP_REFERER'][22::])
    content = {"Lens": product, "line": 426* line, }
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Lens.html", content )

def Lighting(request):
    
    print(request.META['HTTP_REFERER'][22::])
    
    product = lightings.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    content = {"Lightings": product, "line": 426* line}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Lightings.html", content )

def Tripods(request):
    
    
    print(request.META['HTTP_REFERER'][22::])
    
    product = tripods.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    content = {"Tripods": product, "line": 426* line}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/Tripods.html", content )


def binoculars(request):
    
    print(request.META['HTTP_REFERER'][22::])
    
    product = Binoculars.objects.all()
    line = (len(product.values())//4+1)
    if len(product.values()) % 4 == 0:
        line = line -1
    content = {"Binoculars": product, "line": 426* line}
    
    global CONTENT_FLAG
    if CONTENT_FLAG == True:
        content['some_flag'] = True
        CONTENT_FLAG = False
    
    return render(request, "Main/URLS/binoculars.html" , content)
##########################################################
def Camera_product(request, cam_id):
    Camera_product = Camera.objects.get(id=cam_id)
    font_bool = len(Camera_product.name) + len(Camera_product.firm)
    
    
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    quant = Cart(request).productq(str(id))
    
    
    mapper= {"Camera": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form}
    
    
    
    return render(request, "Main/URLS_2/product_camera.html", mapper)


#################################################################
def Lens_product(request, lens_id):
    Camera_product = lens.objects.get(id=lens_id)
    font_bool = len(Camera_product.name)
    
    
    if Camera_product.stock < 21:
        pquant = Camera_product.stock + 1
        cart_product_form = CartAddProductsForm(pquant=pquant)
    else:
        pquant = 21
        cart_product_form = CartAddProductsForm()
    quant = Cart(request).productq(str(id))
    
    mapper= {"Lens": Camera_product, "font_bool": font_bool, "quant": quant ,"FORM_TO_BACKET":cart_product_form}
    
    
    return render(request, "Main/URLS_2/lens_product.html", mapper)
    
def Tripods_product(request, trip_id):
    Camera_product = tripods.objects.get(id=trip_id)
    font_bool = len(Camera_product.name)
    mapper= {"Trip": Camera_product, "font_bool": font_bool}
    return render(request, "Main/URLS_2/trip_product.html", mapper)
    

def Lighting_product(request, Lighting_id):
    Camera_product = lightings.objects.get(id=Lighting_id)
    font_bool = len(Camera_product.name)
    mapper= {"lightings": Camera_product, "font_bool": font_bool}
    return render(request, "Main/URLS_2/lightings_product.html", mapper)
    
    
def Binoculars_product(request, Binoculars_id):
    Camera_product = Binoculars.objects.get(id=Binoculars_id)
    font_bool = len(Camera_product.name)
    mapper= {"Binoculars": Camera_product, "font_bool": font_bool}
    return render(request, "Main/URLS_2/Binoculars_product.html", mapper)

