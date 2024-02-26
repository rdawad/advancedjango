from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormClass
from .models import Mobile,Specification , Place, Restaurant,Article,Plublication

def index(request):
    return HttpResponse("my first backend view")

def login(request):
    return HttpResponse("<h1>this is login page</h1>")    

def home(request):
    details = Mobile.objects.all()
    context = {"contextdetail":details}
    return render(request,"mobile.html",context)

def specs(request):

    specification = Specification.objects.all() 
    context = {"specs":specification}
    return render(request,"specifications.html",context)    

def djangoforms(request):
    context = {"form":form}
    return render(request,"forms.html")

def MyRestaurant(request):
    res = Restaurant.objects.all()
    context = {'restaurant':res}
    return render(request,"restaurant.html",context)

def manytomanyview(request):
    article = Article.objects.all()
    context = {"article":article}
    return render(request,"article.html",context)


