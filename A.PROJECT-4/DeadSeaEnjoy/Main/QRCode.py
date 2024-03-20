from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import pandas as pd
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

class CreateQRFile:
    def __init__(self) -> None:
        pass
    def create_qr_code(self,data, file_name):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)

    def create_pdf(self,pdf_file, data, data_to_encode ,qr_code_file, dataOfOrder):
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        # Создаем стиль для центрирования текста
        centered_style = ParagraphStyle(name='Centered', alignment='center')
        # Создаем контент для PDF
        content = []
                # Путь к вашему логотипу
        logo = "C:/Users/ASUS/Documents/GitHub/HomeDavid/A.PROJECT-4/DeadSeaEnjoy/Main/static/Main/images/logoEN.png"
        logo_img = Image(logo, width=192, height=70)
        logo_img.hAlign = 'LEFT'
        logo_img.hSpace = 20
        content.append(logo_img)
        # Добавляем отступ после логотипа
        content.append(Spacer(1, 15))
        
        # Добавляем заголовок
        title_text = "<font size=20>FUN DAY VOUCHER</font>"
        content.append(Paragraph(title_text, styles["Title"]))
        content.append(Spacer(1, 20))  # Отступ после заголовка

        # Добавляем описание
        description_text = "<font size=12>Your voucher has been successfully reserved in the system. This documentation contains information about your order, and an attached QR code that confirms a successful transaction through the Dead Sea Enjoy service.  After the purchase on the website, your order will be charged to the club card and an order confirmation will be sent by email. When you arrive at the business, you must present the order confirmation and the club card at the reception office.</font>"
        content.append(Paragraph(description_text, styles["Normal"]))
        content.append(Spacer(1, 20))  # Отступ после описания

        # Добавляем данные о покупателе
        for key, value in data.items():
            key = key.replace('_', ' ').capitalize()
            value = str(value)
            content.append(Paragraph(f"<b>{key}: </b>{value}", styles["Normal"]))
        
        
        
        dataOrder = {
        }
        
        for key , val in dataOfOrder:
            dataOrder[key] = ['First name', val]
            dataOrder[key] = ['Last name', val]
            dataOrder[key] = ['Mail', val]
            dataOrder[key] = ['Phone', val]
            dataOrder[key] = ['People', val]
            dataOrder[key] = ['Children', val]
            dataOrder[key] = ['Food', val]
            dataOrder[key] = ['Massage', val]
             
        
        # Создаем DataFrame из данных
        df = pd.DataFrame(data)
        # Создаем таблицу с помощью Pandas
        table = Table(df.values.tolist())
        # Задаем стиль таблицы
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        space = Spacer(1, 15)
        content.append(space)
        content.append(table)
        self.create_qr_code(data_to_encode, qr_code_file)
        qr_img = Image(qr_code_file, width=150, height=150)
        content.append(qr_img)
        content.append(Spacer(1, 20))  # Отступ после QR кода
        # Добавляем нижнее описание
        footer_text = "<font size=10>Thank you for choosing us Dead Sea Enjoy.</font>"
        content.append(Paragraph(footer_text, styles["Normal"]))
        # Добавляем контент в документ
        doc.build(content)
        return pdf_file


   
data_to_encode = "https://www.youtube.com/"
qr_code_file = "C:/Users/ASUS/Documents/GitHub/HomeDavid/A.PROJECT-4/DeadSeaEnjoy/Main/static/Main/QR/example_qr_code.png"
pdf_file = "C:/Users/ASUS/Documents/GitHub/HomeDavid/A.PROJECT-4/DeadSeaEnjoy/Main/static/Main/QR/example_pdf_with_qr_code.pdf"
data = {
    'First name': 'Lunga',
    'Last name': 'd1sdawdas',
    'Mail': '00000000',
    'Phone': '00000000',
    'Identification Card': '00000000',
    'The date of the order': '00000000',
    'Order Status': 'Confirmed',
    'Payment Confirmation': 'Paid'
    # Добавьте любые другие данные, которые вам нужны
}

dataOfOrder = {
    
}

# Создаем PDF файл с данными
CreateQRFile().create_pdf(pdf_file, data, data_to_encode, qr_code_file, dataOfOrder)

'''
CreateQRFile().create_qr_code(data_to_encode, qr_code_file)
CreateQRFile().create_pdf_with_qr_code(pdf_file, qr_code_file)'''



