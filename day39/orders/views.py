from django.urls import reverse
from turtle import delay
from django.shortcuts import redirect, render
from .models import Order, OrderItem, Product
from .forms import OrderCreateForm, ProfileForm
from cart.cart import Cart
from .tasks import order_created
# Create your views here.

def order_create(request):
    cart= Cart(request)
    if request.method == "POST":
        form= OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product= item["product"], price=item["price"], quantity=item["quantity"] )
                p = item["product"]
                p.stock-= item["quantity"]
                if p.stock == 0 or p.stock < 0:
                    return redirect("Shope:ErrorGetData")
                p.save()
                
            
            cart.clear()
            order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
            #return render(request, "orders/order/created.html", {"order": order})
    else:
        data = {'first_name': 'Ivan', 'last_name': 'Ivanov', 'email': 'a@b.ru'}
        
        form = OrderCreateForm(data)
        
    return render(request, "orders/order/create.html", {"cart": cart, "form":form})     
    


