
from .models import Order
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def order_created(order_id, mail, pdf_FILE, name_file):
    sender = "davidlung822@gmail.com"
    password = "bpvfadsexrgihbbg"
    order = Order.objects.get(id=order_id)
    
    # Создаем объект сообщения
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = mail
    message["Subject"] = f"Successful Quickclick order confirmation. Number order {order_id}"
    
    # Текст сообщения
    text = f"Dear {order.first_name} {order.last_name}, \n\nYour order has been received and we are starting the assembly. Order number:{order_id}\n\n"
    text += "\nOrder Details:\n"
    text += "Order ID:"+ str(order_id) +"\n"+ 'The number of people who have reserved the voucher: ' + str(order.count_people)
    if order.count_children > 0:
        text += '\n'+ 'Children are registered: '+ str(order.count_people) 
    text += '\n' + 'The condition of the general diet: ' + order.food.food +'\n' + 'Spa conditions: ' + order.massage.massage +'\n'+'\n'
    text += "Thank you for choosing us!"
    
    # Добавляем текст сообщения в объект MIMEText
    message.attach(MIMEText(text))
    
    # Открываем и прикрепляем PDF-файл
    with open(pdf_FILE, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={name_file}",  # Замените на имя вашего файла
    )
    message.attach(part)
    
    # Отправляем сообщение
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, mail, message.as_string())
        server.quit()
        return 'The message was sent successfully'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password'