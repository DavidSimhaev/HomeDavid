
from .models import Order
import smtplib
from email.mime.text import MIMEText

def order_created(order_id, mail, cart):
    sender = "davidlung822@gmail.com"
    password = "bpvfadsexrgihbbg"
    order = Order.objects.get(id=order_id)
    
    message = f"Dear {order.first_name}, \n\nYour order has been received and we are starting the assembly. Order number:{order_id}\n\n"
    message = message + "\nOrder Details:\n"
    for elem in cart:
        message+= "Product:"+ str(elem["product"]) +"\t" + "Unit price:" +"\t" + str(elem["price"]) + "\t" + "Quantity:" + str(elem["quantity"]) + "\n"
    message += "\nThank you for choosing us!"
    
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


 
         