from django.urls import reverse
#from turtle import delay
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderCreateForm
from Cart.Cart import Cart
from .tasks import order_created
from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

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
                    return redirect("Main:ErrorGetData")
                p.save()
            
           
            cart.clear()
            
                                 
            #order_created.delay(order.id)
            request.session['order_id'] = order.id # Что то связанно с почтой
            
            order_id = request.session.get('order_id')
            order = get_object_or_404(Order, id=order_id)
            
            success_url = request.build_absolute_uri(reverse('payment:completed',args=[order.id])) 
            cancel_url = request.build_absolute_uri(reverse('payment:canceled')) 
            
            session_data = {
                'mode': 'payment', 
                'client_reference_id': order_id,
                'success_url': success_url,
                'cancel_url': cancel_url,
                'line_items': []
                }
            for item in order.items.all(): 
                
                session_data['line_items'].append(
                    {
                        'price_data': {
                            'unit_amount': int(item.price*Decimal('100')), 
                            'currency': 'usd',
                            'product_data': {
                                'name' : item.product,
                            },
                        },
                        'quantity': int(item.quantity) 
                        
                    }
                )
            session = stripe.checkout.Session.create(**session_data)
            return redirect(session.url, code=303) # 
            
            
            #return render(request, "orders/order/created.html", {"order": order})
    else:
        data = {"user": request.user.id, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email}
        form = OrderCreateForm(data)
        return render(request, "order/create.html", {"cart": cart, "form":form})     
    

