import os
import smtplib
import ssl
from email.message import EmailMessage


HOST = "smtp.gmail.com"
PORT = 587
RECEIVER = "emailexperimental70@gmail.com"
PASSWORD = os.getenv("PASSWORD")


def send_email(user_mail, message):

    # creating email message
    email_message = EmailMessage()
    email_message['Subject'] = "New Tour is Here!"
    email_message.set_content(message)

    # Sending message
    gmail = smtplib.SMTP(HOST, PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(RECEIVER, PASSWORD)
    gmail.sendmail(user_mail, RECEIVER, email_message.as_string())
    gmail.quit()
