from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Номер заказа: {order_id}"
    message = f"Уважаемый(ая) {order.first_name}, \n\n Ваш заказ получен и мы приступаем к сборке. Номер заказа:{order_id}\n"
    mail_sent = send_mail(subject, message, "admin@retailtea.co.il", [order.email] )
    return mail_sent


 
         