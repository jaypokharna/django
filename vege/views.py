from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.http import HttpResponse    

# Create your views here.

def receipes(request):
    if request.method == "POST":

        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Reci.objects.create(

            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image

        )

        return redirect('/vege/')
    
    queryset = Reci.objects.all()
    context = {"receipes" : queryset}

    return render(request,"receipes.html",context)


def delete_item(request,id):
    print(id)
    queryset = Reci.objects.get(id=id)
    queryset.delete()
    return redirect('/vege/')

def update_item(request,id):
    queryset = Reci.objects.get(id=id)
    context = {"receipe" : queryset}
    return render(request,"update_item.html",context)
