
from .models import Order
import smtplib
from email.mime.text import MIMEText

def order_created(order_id, mail):
    sender = "davidlung822@gmail.com"
    password = "bpvfadsexrgihbbg"
    order = Order.objects.get(id=order_id)
    
    message = f"Dear {order.first_name} {order.last_name}, \n\nYour order has been received and we are starting the assembly. Order number:{order_id}\n\n"
    message = message + "\nOrder Details:\n"
    message+= "Order ID:"+ str(order_id) +"\n"+ 'The number of people who have reserved the voucher: ' + str(order.count_people)
    
    if order.count_children > 0:
        message+='\n'+ 'Children are registered: '+ str(order.count_people) 
    message+='\n' + 'The condition of the general diet: ' + order.food.food +'\n' + 'Spa conditions: ' + order.massage.massage +'\n'+'\n'
     
    message += "Thank you for choosing us!"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = f"Successful Quickclick order confirmation. Number order {order_id}"
        server.sendmail(sender, mail, msg.as_string())
        
        return 'The message was sent successfully'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password'
    
#    mail_sent = send_mail(subject, message, "admin@retailtea.co.il", [order.email] )
#    return mail_sent
