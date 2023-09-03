from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def login(request):

    if request.method=='POST':
        emails = request.POST.get('email')
        password = request.POST.get('password')

        queryset = Signup.objects.all()
        for i in queryset:

            if emails == i.email:
                return HttpResponse("Success")
            else:
                print("Incorrect Email")


    return render(request,"login.html")


def signup(request):

    if request.method=='POST':
        
        Signup.objects.create(
            fullname = request.POST.get('fullname'),
            email = request.POST.get('email'),
            phnumber = request.POST.get('phnumber'),
            password = request.POST.get('password')
        )
        return redirect ('/login/')


    return render(request,"signup.html")