from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from mysite import settings
#from . tokens import generate_token


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

        #user verification
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists. Please try a different username")
            return redirect('home')

        if User.objects.filter(email = email):
            messages.error(request, "Email already registered")
            return redirect('login')

        if len(username) > 10:
            messages.error(request, "The username should be less than 10 characters")
        if pass1 != pass2:
            messages.error(request,"passwords didnt match")
            return redirect('home')
       
        if not username.isalnum():
            messages.error(request,"Username must be alpha-numeric ")   
            return redirect('home')


        myuser = User.objects.create_user(username, email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        

        #Welcome Email
        subject = "Welcome to KodeSprint"
        message = "Hello" + myuser.first_name  + "!!  \n" + "Welcome to KodeSprint!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThank You\nMansi Sonawani"
        from_email = settings.EMAIL_HOST_USER
    return render(request, "authentication/signup.html")        
             
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully! ")
    return redirect('home')
    

