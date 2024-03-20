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
        content.append(Spacer(1, 10))
        
        # Добавляем заголовок
        title_text = "<font size=20>FUN DAY VOUCHER</font>"
        content.append(Paragraph(title_text, styles["Title"]))
        content.append(Spacer(1, 15))  # Отступ после заголовка

        # Добавляем описание
        description_text = "<font size=12>Your voucher has been successfully reserved in the system. This documentation contains information about your order, and an attached QR code that confirms a successful transaction through the Dead Sea Enjoy service.  After the purchase on the website, your order will be charged to the club card and an order confirmation will be sent by email. When you arrive at the business, you must present the order confirmation and the club card at the reception office.</font>"
        content.append(Paragraph(description_text, styles["Normal"]))
        content.append(Spacer(1, 10)) 

        for i, (key, value) in enumerate(data.items()):
            key = key.replace('_', ' ').capitalize()
            value = str(value)
            if i == len(data) - 1:  
                content.append(Paragraph(f"<b>{key}: </b><font color='green'><b>{value}</b></font>", styles["Normal"]))
            else:
                content.append(Paragraph(f"<b>{key}: </b>{value}", styles["Normal"]))
        dataOrder = {
        }
        for key in dataOfOrder.keys():
            dataOrder[key] = [key, dataOfOrder[key]]
        # Создаем DataFrame из данных
        df = pd.DataFrame(dataOrder)
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
        content.append(Spacer(1, 15))  
        
        content.append(qr_img)
        
        footer_text = "<font size=10>Please note that in case of non-attendance at the event, the voucher can be rescheduled to any other day before DD-MM-XX. To reschedule the event, the day before the event starts</font>"
        content.append(Paragraph(footer_text, styles["Normal"]))
        content.append(Spacer(1, 22))  
        
        footer_style = ParagraphStyle(
            "FooterStyle",
            fontSize=10,
            alignment=2  # Значение 2 соответствует выравниванию по правому краю
        )
        
        footer_text2 = "Tel: 08-6689999"
        content.append(Paragraph(footer_text2, footer_style))
        content.append(Spacer(1, 3))  
        
        footer_text3 = "Fax: 08-6689900"
        content.append(Paragraph(footer_text3, footer_style))
        content.append(Spacer(1, 3))   
        
        footer_text4 = "dds.op@ichotels.co.il"
        content.append(Paragraph(footer_text4, footer_style))
        content.append(Spacer(1, 3))   
        
        
        footer_text6 = "www.enjoydeadsea.com."
        content.append(Paragraph(footer_text6, footer_style))
        content.append(Spacer(1, 5))
        
        # Добавляем контент в документ
        doc.build(content)

        return qr_code_file 
        