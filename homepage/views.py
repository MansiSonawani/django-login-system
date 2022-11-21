from cgitb import html
from re import template
from django.http import HttpResponse
from django.template import Template, context
from django.shortcuts import render

def Main(request):
    return render("homepage/Main.html")

def Profile(request):
    return render(request, "homepage/Profile.html")   

def Points(request):
    return render(request, "homepage/Points.html")     

def Task(request):
    return render(request, "homepage/Task.html") 

def Logout(request):
     pass






    


