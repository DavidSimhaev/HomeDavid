from django.shortcuts import render, redirect, get_object_or_404 , resolve_url, reverse # Почему у меня reverse беленьким подчеркивается?

from decimal import Decimal
import stripe
from django.conf import settings
from orders.models import Order
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    breakpoint()
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed')) # Не понял    build_absolute_uri
        cancel_url = request.build_absolute_uri(reverse('payment:canceled')) # Не понял build_absolute_uri
        
        session_data = {
            'mode': 'payment', 
            'client_reference_id': order_id,
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        for item in order.items.all(): # Не понял items.all()
            session_data['line_items'].append(
                {
                    'price_data': {
                        'unit_amount': int(item.price*Decimal('100')), # Вроде привращаем в целое число
                        'currency': 'usd',
                        'product_data': {
                            'name' : item.product.name,
                        },
                    },
                    'quantity': item.quantity 
                    
                }
            )
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303) # session url это? code = 303 это что? 
    else:
        return render(request, 'payment/process.html', locals()) # Кто такой локалс , где мы его импортировали?
    
def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')

