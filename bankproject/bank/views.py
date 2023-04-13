from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from bank.models import Task


# from .forms import BookingForm
#
# from .models import Departments, Doctors
# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginin(request):
    return render(request, 'loginin.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        cpassword = request.POST['psw1']
        user = User.objects.create_user(username,password,cpassword)
        user.save()
        messages.success(request,"Account has been created successfully")
        return redirect("login")
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        dob = request.POST.get('dob', '')
        age=request.POST.get('age','')
        gender=request.POST.get('gender','')
        phonenumber=request.POST.get('phonenumber','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        district=request.POST.get('district','')
        branch=request.POST.get('branch','')
        acc_type=request.POST.get('acc_type','')
        material=request.POST.get('material','')
        task=Task(name=name,dob=dob,age=age,gender=gender,phonenumber=phonenumber,email=email,address=address,district=district,branch=branch,acc_type=acc_type,material=material)
        task.save()
        messages.success(request,"Application accepted")
        return redirect("home")
    return render(request, 'add.html',{'task1': task1})