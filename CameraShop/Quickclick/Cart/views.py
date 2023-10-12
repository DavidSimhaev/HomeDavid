import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .names_filtred import Names_Filtred

# Create your views here.

from django.views.decorators.http import require_POST
from Main.models import Camera, lens, tripods, lightings, Binoculars
from .Cart import Cart
from .forms import CartAddProductsForm
import ast

@require_POST
def cart_add(request, product_id):
    
    try:
        cart = Cart(request)
        res = cart.check_request()
        dict = { "Camera": Camera, "lens": lens, "tripods": tripods, "lightings": lightings , "Binoculars": Binoculars } 
        if res in ("Filtred_Camers", "Lens_filtred", "Lightings_filtred", "Tripods_filtred", "binoculars_filtred"):
            res = Names_Filtred(res).replace_name_filtred()
        product = get_object_or_404(dict[res], id=product_id)
        
        form = CartAddProductsForm(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            cart.add(product=product,quantity=cd['quantity'], override_quantity=cd['override'])
        #breakpoint()
        
        response= redirect('Cart:cart_detail')
        
        response.set_cookie(str(request.user.id), cart.cart)
        
        return response
    except ObjectDoesNotExist:
        return redirect('/')

@require_POST
def cart_remove(request, obj_product, product_id):

    
    cart = Cart(request)
    dict = { "Camera": Camera, "lens": lens, "tripods": tripods, "lightings": lightings , "Binoculars": Binoculars } 

    
    product = get_object_or_404(dict[obj_product], id=product_id)
    cart.remove(product, obj_product)
    response= redirect('Cart:cart_detail')
        
    response.set_cookie(str(request.user.id), cart.cart)
        
    return response



def cart_detail(request):
    
    cart = Cart(request)
    l=[]
    for i in request.META['HTTP_REFERER'][22::]:
        if i == "/":
            break
        l.append(i)
    res = "".join(l)
    if res == "Camers":
        res = "Camera"
    if res == "Lens":
        res = "lens"
    if res == "Tripods":
        res = "tripods"
    if res == "Lightings":
        res = "lightings"
    if res == "binoculars":
        res = "Binoculars"
    print(cart.cart)    
    try:
        cart.cart= ast.literal_eval(request.COOKIES.get(f'{request.user.id}'))
    except:
        pass
    return render(request, "Cart/Cart.html", {"Cart": cart})
    
