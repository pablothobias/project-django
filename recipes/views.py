from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "home.html")


def about_view(request):
    return HttpResponse("<h1>About Page</h1>")


def contact_view(request):
    return HttpResponse("<h1>Contact Page</h1>")
