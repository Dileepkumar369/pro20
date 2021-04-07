from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>HI from index of app1</h1>")
def page(request):
    return render(request,"sample1.html")

# Create your views here.
