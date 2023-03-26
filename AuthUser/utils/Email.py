import uuid
from django.core.mail import send_mail

def send_email(email,otp):

    subject = 'Email verification'
    myuuid = uuid.uuid4()
    # print(email)
    
    message = "your otp is "+str(otp)
    email_from = 'amal76735@gmail.com'
    
    recipient_list=[email]
    
    send_mail( subject, message, email_from ,recipient_list)


