from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>starts to index of app2</h1>")
def page2(request):
    return render(request,"sample2.html")

# Create your views here.
