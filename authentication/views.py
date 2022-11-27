from cgitb import html
from re import template

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as Django_login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Template, context


def home(request):
    return render(request ,"authentication/index.html")

def signup(request):
    if request.method == "POST" :
        username = request.POST.get('username')  
        fname = request.POST.get('fname')  
        lname = request.POST.get('lname')  
        email = request.POST.get('email')  
        pass1 = request.POST.get('pass1')  
        pass2 = request.POST.get('pass2')  
        
        myuser = User.objects.create_user(username, email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('Django_login')

    return render(request, "authentication/signup.html")        
             
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username= username, password = pass1)
        
        if user is not None:
            Django_login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request,"Bad credentials") 
            return redirect('home')   

    return render(request, "authentication/login.html")     

def logout(request):
    logout(request)
    messages.success(request, "logged out successfully! ")
    return redirect('home')
    

