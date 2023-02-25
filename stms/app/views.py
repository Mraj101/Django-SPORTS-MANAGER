from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth

from app.models import Registration





# Create your views here.

def home(request):
    return render(request,'app/index.html')

def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        gender=request.POST['gender']
        age=request.POST['age']
        phone_number=request.POST['phone_number']
        catalogue=request.POST['catalogue']
        myuser=Registration(name=name,email=email,password1=password1, password2=password2,gender=gender,age=age,phone_number=phone_number,catalogue=catalogue)
        myuser.save()
    return render(request,'app/index.html')



def login(requset):
    pass




