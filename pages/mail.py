import os
import smtplib
from email.message import EmailMessage
def send_mail(message, email, subject, ):
    MAIL_USERNAME = "amdigitalfurniture@gmail.com"
    EMAIL_PASS = "amdigital@2020"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = MAIL_USERNAME
    #Start the Context Manager to automatically manage the server Conncetion
    msg.set_content("Message from Site")
    msg.add_alternative(message, subtype="html")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            #Since we have identified ourselves as secure connection we can now login
            smtp.login(MAIL_USERNAME, EMAIL_PASS)
            #Send Mail
            smtp.send_message(msg)
        print ("--Email Success--")
    except ConnectionRefusedError:
        print("Please try Again...Email Unsuccessful")