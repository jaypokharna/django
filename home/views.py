from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    people = [
        {"name":"Jay" , "age":21 },
        {"name":"Yogita" , "age":21 },
        {"name":"Venkatesh" , "age": 17},
        {"name":"Guatam" , "age": 22},
        {"name":"Sakshi" , "age":16 },
    ]

    return render(request,"index.html",context={ "people" : people })

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")