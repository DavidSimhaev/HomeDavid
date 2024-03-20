from time import sleep
from django.shortcuts import render
from .models import Order, Food, Massage
# Create your views here.
from django.urls import reverse
#from turtle import delay
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, OrderItem, ORDER_ID
from .tasks import order_created
from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render
from .QRCode import CreateQRFile
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION
from django.http import HttpResponseRedirect
import random
import os

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
    passport_id = request.GET.get('passport_id')
    dateEventHolidayOrNot = request.GET.get('dateEventHolidayOrNot')
    
    def risez(word):
        new_word= ''
        for sym in word:
            if sym == ':':
                break
            new_word +=sym
        return new_word
    
    new_food= risez(food)
    new_massage= risez(massage)
    
    
    people = people[0]    
        
    
    if new_massage == 'No' or new_massage == '':
        new_massage = 0
        
    if children == 'No' or children == '':
        children = 0
    else:
        children = int(children[0]) 
    
    
    if dateEventHolidayOrNot == 'Saturday' or dateEventHolidayOrNot == 'Friday':
        price += 70
        
    if new_food == 'Breakfast' or new_food == 'Lunch':
        price += 120 * int(people)
        price += 100 * int(children)
    else:
        if new_food == 'Breakfast   Lunch' or new_food == 'Breakfast+Lunch':
            price += 240 * int(people)
            price += 200 * int(children)
        elif new_food == 'Coffee and pastry':
            price += 50 * int(people)
            price += 30 * int(children)
        elif new_food == 'Wine and fruits':
            price += 80 * int(people)
    if int(people) == 1:
        #people = 'Fun Day for a single'
        price += 160
        if int(new_massage) == 30:
            price +=100
        elif int(new_massage) == 50:
            price +=200        
    elif int(people) == 2:
        #people = 'Fun Day for a couple'
        price += 300
        if int(new_massage) == 30:
            price +=200
        elif int(new_massage) == 50:
            price +=400
    elif int(people) > 2:
        price += int(people) * 150
        #people += ' people'
    if new_massage == 0:
        new_massage = 'No'
    if children == 0:
        children = 'No'
        
        
    mapper = { 'Date': dateEvent,
              'Date_Label': Date_Label,
              'people':people, 
              'children': children,
              'meal' : new_food,
              'massage': massage,
              'name': name ,
              'last': last ,
              'mail': mail,
              'numberID': numberID,
              'price': price,    
              'passport_id': passport_id         
            }
    return render(request, "WriteDateCustemer.html", mapper)

def PaymentProcces(request):
    Date = request.GET.get('Date')
    people = request.GET.get('select3')
    children = request.GET.get('select4')
    food  = request.GET.get('select1')
    massage = request.GET.get('select2')
    name = request.GET.get('id_name')
    last = request.GET.get('id_last')
    mail = request.GET.get('mail_var')
    numberID = str(request.GET.get('numberID'))
    passport_id = request.GET.get('passport_id')
    Date_Label = str(request.GET.get('date_lab'))
    price = request.GET.get('price_ID')[:-1]
    
    def backsize(word):
        if word == 'Breakfast':
            return 'Breakfast: (Person-120₪/Child-100₪)'
        elif word == 'Breakfast+Lunch':
            return 'Breakfast+Lunch: (Person-240₪/Child-200₪)'
        elif word == 'Coffee and pastry':
            return 'Coffee and pastry: (40₪)'
        elif word == 'Lunch':
            return 'Lunch: (Person-120₪/Child-100₪)'
        elif word == 'Wine and fruits':
            return 'Wine and fruits: (90₪)'
        elif word == ' 30 minutes':
            return '30 minutes: (100₪)'
        elif word == ' 45 minutes':
            return '45 minutes: (200₪)'
        elif word == ' 50 minutes':
            return '50 minutes: (210₪)'
        return word
    
    
    if food == 'Breakfast Lunch':
        FoodObj = Food.objects.get(food='Breakfast: (Person-120₪/Child-100₪)')
    else:
        food = backsize(food)
        FoodObj = Food.objects.get(food=food)
    if children == ' No' or children == '' or children == 'No':
        children = 0
    if massage == ' No' or massage == 'No' or massage == '':
        MassageObj = Massage.objects.get(massage= 'No')
    else:
        massage = backsize(massage)
        MassageObj = Massage.objects.get(massage= massage)
    if people == ' Fun Day for a single ':
        people = '1'
    elif people == ' Fun Day for a couple ':
        people = '2'
    elif 'people' in people :
        people = people[0]  
    order = Order.objects.create(Date = Date, first_name=name, last_name = last, email = mail, phone = numberID, passport= passport_id, count_people = people, count_children= children, food = FoodObj, massage = MassageObj, boolweekends = False )    
    
    
    
    while True:
        try:        
            random_number = random.randint(0, 999999999)
            ID_ORDER = ORDER_ID.objects.get(indificator=random_number) 
        except:    
            break    
    ID_ORDER = ORDER_ID.objects.create(indificator=random_number) 
    OrderItem.objects.create(ORDER_ID= ID_ORDER,order= order , product= Date_Label+ ' Fun Day', price=price, quantity=1 , paid = False)
    request.session['order_id'] = name + ' ' + last
    order_id = request.session.get('order_id')
    success_url = request.build_absolute_uri(reverse('Main:payment_completed') + '?order_id=' + str(order.id) + '&UNIC_ID='+ str(ID_ORDER.indificator) +'&Date_Label=' + Date_Label ) 
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
    Date_Label = request.GET.get('Date_Label')
    order_id = request.GET.get('order_id')
    
    ID_ORDER = request.GET.get('UNIC_ID')
    order = Order.objects.get(id=order_id)
    
    
    
    data_to_encode = "https://www.youtube.com/"
    
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    qr_code_file = os.path.join(base_dir, 'media', f'example_qr_code_{ID_ORDER}.png').replace('\\','/')
    pdf_file = os.path.join(base_dir, 'media', f'vocher_{ID_ORDER}.pdf').replace('\\','/')
    ObjId = ORDER_ID.objects.get(indificator = ID_ORDER)
    DATE_ORDER = OrderItem.objects.get(ORDER_ID= ObjId)
    data_Contact = {
        'First name': order.first_name,
        'Last name': order.last_name, 
        'Mail': order.email ,
        'Phone': order.phone ,
        'Identification Card': order.passport,
        'Date of the event': Date_Label,
        'Order Status': 'Confirmed',
        'Payment Confirmation': 'Paid'
    }
    if order.count_children == '0' or order.count_children == 0:
        valChildren = 'No'
    else:
        valChildren = order.count_children
    dataOfOrder= {
        "ID": ID_ORDER,
        'Date': Date_Label ,
        'People': order.count_people ,
        'Food': str(order.food)[:int(str(order.food).find(':'))] ,
        'Children': valChildren ,
        'Massage': str(order.massage)[:int(str(order.massage).find(':'))],
        'Price': str(DATE_ORDER.price) + ' ILS'
                  }
    CreateQRFile().create_pdf(pdf_file, data_Contact, data_to_encode, qr_code_file, dataOfOrder)
    
    
    
    
    DATE_ORDER.pdf_file = f'vocher_{ID_ORDER}.pdf'  # Это должен быть путь к файлу
    DATE_ORDER.save()
    
    order_created(order.id, order.email,pdf_file, DATE_ORDER.pdf_file)
    pdf_file_path = str(settings.MEDIA_URL) + str(DATE_ORDER.pdf_file)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    mapper = {'DATE_ORDER': pdf_file_path, 'DETAIL_ORDER': order}
    return render(request, 'completed.html', mapper)

def payment_canceled(request):
    return render(request, 'canceled.html')