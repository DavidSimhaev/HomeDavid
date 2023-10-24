
from .models import Order
import smtplib
from email.mime.text import MIMEText
import os
def order_created(order_id):
    sender = "davidlung822@gmail.com"
    password = "bpvfadsexrgihbbg"
    order = Order.objects.get(id=order_id)
    subject = f"Номер заказа: {order_id}"
    message = f"Уважаемый(ая) {order.first_name}, \n\n Ваш заказ получен и мы приступаем к сборке. Номер заказа:{order_id}\n"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE"
        server.sendmail(sender, "davidlunga822@gmail.com", msg.as_string())
        
        return 'The message was sent successfully'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password'
    
#    mail_sent = send_mail(subject, message, "admin@retailtea.co.il", [order.email] )
#    return mail_sent


 
         