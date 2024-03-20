from django.shortcuts import render
from .models import Order, Food, Massage
# Create your views here.
from django.urls import reverse
#from turtle import delay
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, OrderItem
from .tasks import order_created
from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render
#from .QRCode import CreateQRFile
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION
from django.http import HttpResponseRedirect


def Main(request):
    return render(request, "Main.html")

def FunDay(request):
    listFood = Food.objects.all()
    listMassage = Massage.objects.all()
    mapper = {'listFood': listFood, 'listMassage': listMassage}
    return render(request, "FunDay.html", mapper)

def WriteDateCustemer(request):
    price = 0
    people = request.GET.get('select3')
    children = request.GET.get('select4')
    food = request.GET.get('select1')
    massage = request.GET.get('select2')
    name = request.GET.get('id_name')
    last = request.GET.get('id_last')
    mail = request.GET.get('id_mail')
    numberID = str(request.GET.get('numberID'))
    Date_Label = str(request.GET.get('Date_Label'))
    dateEvent = request.GET.get('dateEvent')
    dateEventHolidayOrNot = request.GET.get('dateEventHolidayOrNot')
    if massage == 'Absent':
        massage = 0
    if children == 'Absent':
        children = 0
    if dateEventHolidayOrNot == 'Saturday' or dateEventHolidayOrNot == 'Friday':
        price += 70
    if int(people) == 1:
        price += 160
        if int(massage) == 30:
            price +=100
        elif int(massage) == 50:
            price +=200        
    elif int(people) == 2:
        price += 300
        if int(massage) == 30:
            price +=200
        elif int(massage) == 50:
            price +=400
    if food == 'Breakfast' or food == 'Lunch':
        price += 120 * int(people)
        price += 100 * int(children)
    else:
        if food == 'Breakfast   Lunch':
            price += 240 * int(people)
            price += 200 * int(children)
        elif food == 'Coffee and pastry':
            price += 50 * int(people)
            price += 30 * int(children)
        elif food == 'Wine and fruits':
            price += 80 * int(people)
    mapper = { 'Date': dateEvent,
              'Date_Label': Date_Label,
              'people':people, 
              'children': children,
              'meal' : food,
              'massage': massage,
              'name': name ,
              'last': last ,
              'mail': mail,
              'numberID': numberID,
              'price': price,             
            }
    return render(request, "WriteDateCustemer.html", mapper)

def PaymentProcces(request):
    Date = request.GET.get('Date')
    people = request.GET.get('select3')
    children = request.GET.get('select4')
    food = request.GET.get('select1')
    massage = request.GET.get('select2')
    name = request.GET.get('id_name')
    last = request.GET.get('id_last')
    mail = request.GET.get('mail_var')
    numberID = str(request.GET.get('numberID'))
    Date_Label = str(request.GET.get('date_lab'))
    price = request.GET.get('price_ID')[:-1]
    
    FoodObj = Food.objects.get(food= food)
    MassageObj = Massage.objects.get(massage= massage)
    order = Order.objects.create(Date = Date, first_name=name, last_name = last, email = mail, phone = numberID, count_people = people, count_children= children, food = FoodObj, massage = MassageObj, boolweekends = False )    
    OrderItem.objects.create(order= order , product= Date_Label+ ' Fun Day', price=price, quantity=1 )
    order_created(order.id, order.email)
    request.session['order_id'] = name + ' ' + last
    order_id = request.session.get('order_id')
    
    
    
    
    
    success_url = request.build_absolute_uri(reverse('Main:payment_completed') + '?order_id=' + str(order.id)) 
    cancel_url = request.build_absolute_uri(reverse('Main:payment_canceled')) 
    session_data = {
        'mode': 'payment', 
        'client_reference_id': order_id,
        'success_url': success_url,
        'cancel_url': cancel_url,
        'line_items': []
        }
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    for line_item in session_data['line_items']:
        print("Unit amount:", line_item['price_data']['unit_amount'])
    for item in order.items.all(): 
        session_data['line_items'].append(
            {
                'price_data': {
                    'unit_amount': int(item.price*Decimal('100')), 
                    'currency': 'ils',
                    'product_data': {
                        'name' : item.product,
                    },
                },
                'quantity': int(item.quantity) 
                
            }
        )
    session = stripe.checkout.Session.create(**session_data)
    return redirect(session.url, code=303) # 

def payment_completed(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    
    
    data_Contact = {
        'First name': order.first_name,
        'Last name': order.last_name, 
        'Mail': order.email ,
        'Phone': order.phone ,
        'Identification Card': '00000000',
        'The date of the order': '00000000',
        'Order Status': 'Confirmed',
        'Payment Confirmation': 'Paid'
        
    }



    dataOfOrder= {
        "ID": 1,
        'Date': order.Date ,
        'People': order.count_people ,
        'Children': order.count_people ,
        'Food': order.food ,
        'Massage': order.massage,
        'Price': order.massage
                  }
    

    #pdfFile = CreateQRFile().create_pdf(pdf_file, data, data_to_encode, qr_code_file, dataOfOrder) 
    
    data_to_encode = "https://www.youtube.com/"
    qr_code_file = "C:/Users/ASUS/Documents/GitHub/HomeDavid/A.PROJECT-4/DeadSeaEnjoy/Main/static/Main/QR/example_qr_code.png"
    pdf_file = "C:/Users/ASUS/Documents/GitHub/HomeDavid/A.PROJECT-4/DeadSeaEnjoy/Main/static/Main/QR/example_pdf_with_qr_code.pdf"

    
    
    
    return render(request, 'completed.html')

def payment_canceled(request):
    return render(request, 'canceled.html')