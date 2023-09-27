from home.models import *
import time
from django.core.mail import send_mail,EmailMessage
from django.conf import settings




def send_email_to_client(subject,message,recipient):
    # print(subject,message,recipient)
    from_email = "Jay Pokharna"
    recipient_list = [recipient]
    send_mail(subject , message , from_email , recipient_list )


def send_email_with_attachment(subject,message,recipient,file_path):
    print("Sending Email")
    mail = EmailMessage(subject=subject,body=message,from_email = "Jay Pokharna", 
                       to = [recipient] )
    
    mail.attach_file(file_path)
    mail.send()
    print("Email Sent")
     