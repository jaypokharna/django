from django.shortcuts import render,redirect
from django.http import HttpResponse
from .util import send_email_to_client,send_email_with_attachment
from django.conf import settings
# Create your views here.

def home(request):

    if request.method == "POST":
        print("Receiving Data")
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')
        file_path = f"{settings.BASE_DIR}/trial.py"
        # send_email_with_attachment(subject,message,recipient,file_path)
        print("Data Received")
        # send_email_with_attachment(subject,message,recipient)
        send_email_to_client(subject,message,recipient)
        return redirect('/')

    return render(request,"index.html")
    
def send_email():
    return redirect('/')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")