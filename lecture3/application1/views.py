from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "application1/index.html")

def master(request):
    return HttpResponse('Hello master Phase, this is a response!')

def greet(request, name):
    return render(request, "application1/greet.html", {
        "name": name.capitalize()
    })