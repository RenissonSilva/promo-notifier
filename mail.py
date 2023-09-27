from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

class mail():
    def send_mail(html:str):
        load_dotenv()

        mail = os.getenv('mail')
        password = os.getenv('password')
        server = 'smtp.gmail.com:587'

        message = MIMEMultipart(
            "alternative", None, [MIMEText(html,'html')])

        message['Subject'] = "Promoção s23 Ultra"
        message['From'] = mail
        message['To'] = mail
        server = smtplib.SMTP(server)
        server.ehlo()
        server.starttls()
        server.login(mail, password)
        server.sendmail(mail, mail, message.as_string())
        server.quit()