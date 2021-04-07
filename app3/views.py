from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>views of index from app3</h1>")
def page3(request):
    return render(request,"sample1.html")

def through_data(request,data):
    return HttpResponse(f'<h1>The Recieved data is {data}</h1>')
# Create your views here.
