import json
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

from django.views.decorators.http import require_POST
from Main.models import Camera, lens, tripods, lightings, Binoculars
from .Cart import Cart
from .forms import CartAddProductsForm

@require_POST
def cart_add(request, product_id):
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
    
    dict = { "Camera": Camera, "lens": lens, "tripods": tripods, "lightings": lightings , "Binoculars": Binoculars } 
    
    cart = Cart(request)
    product = get_object_or_404(dict[res], id=product_id)
    form = CartAddProductsForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'], override_quantity=cd['override'])
    #breakpoint()
    return redirect('Cart:cart_detail')





def cart_detail(request):
    cart = Cart(request)
    return render(request, "Cart/Cart.html", {"Cart": cart})
    
