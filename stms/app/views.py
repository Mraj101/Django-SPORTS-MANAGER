from django.shortcuts import render,redirect

from django.forms import inlineformset_factory
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request,'app/index.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user=User.objects.create_user(username=name,password=password1,email=email,)
        user.save()
        return redirect('/')
    else:
        return render(request,'index.html')



