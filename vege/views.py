from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.http import HttpResponse   
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

@login_required(login_url = "/login/")
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

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
        print(queryset)

    context = {"receipes" : queryset}

    return render(request,"receipes.html",context)

@login_required(login_url = "/login/")
def delete_item(request,id):
    print(id)
    alibaba = Reci.objects.get(id=id)
    alibaba.delete()
    return redirect('/vege/')

@login_required(login_url = "/login/")
def update_item(request,id):
    queryset = Reci.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        queryset.receipe_name=data.get('receipe_name')
        queryset.receipe_description=data.get('receipe_description')

        receipe_image = request.FILES.get('receipe_image')
        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()

        return redirect('/vege/')


    context = {"receipe" : queryset }
    return render(request,"update_item.html",context)

def login_page(request):
    
    if request.method == "POST":

        uname = request.POST.get("uname")
        password = request.POST.get("password")

        if not User.objects.filter(username = uname):
            messages.info(request,"Invalid Username")
            return redirect("/login/")
        
        user = authenticate(username = uname , password = password)

        if user is None:
            messages.info(request , "Wrong Password")
            return redirect("/login/")
        else:
            login(request , user)
            return redirect("/vege/")
        
    return render(request,"login.html")

def signup(request):  # sourcery skip: last-if-guard
    if request.method == "POST":
        
        user = User.objects.filter(username = request.POST.get("uname"))

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/signup/")

        user = User.objects.create(
            first_name = request.POST.get("fname"),
            last_name = request.POST.get("lname"),
            username = request.POST.get("uname")
        )
        print(request.POST.get("password"))

        user.set_password(request.POST.get('password'))
        user.save()
        messages.info(request,"Account created successfully")

        return redirect("/signup/")

    return render(request,"signup.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")  

def get_students(request):

    queryset = Student.objects.all()

    # print(ranks)

    if request.GET.get('search'):
        search = request.GET.get('search')
        # queryset = queryset.filter(student_name__icontains = search )
        queryset = queryset.filter(

            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search)
         )

        paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "report/report.html", {"queryset": page_obj,"search":search})
    
    else:
        paginator = Paginator(queryset, 10)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(request, "report/report.html", {"queryset": page_obj})
    
from vege.models import *

# One way of checking the rank - Dynamically generating rank everytime when you click on student_id
# def see_marks(request,student_id):
#     queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
#     total = queryset.aggregate(total=Sum('marks'))
#     current_rank = -1
#     ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
#     i=1
#     for rank in ranks:
#         if student_id == rank.student_id.student_id:
#             current_rank = i
#             break
#         else:
#             i+=1

#     return render(request , 'report/checkresult.html',context={'queryset' : queryset,'total':total,'rank':current_rank})

def see_marks(request,student_id):
   
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total = queryset.aggregate(Sum('marks'))
    print(queryset)
    
    return render(request , 'report/checkresult.html',context={'queryset' : queryset,'total':total})