from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    context = {"name": "Pablo Thobias"}
    return render(request, "recipes/pages/home.html", context=context)


def about_view(request):
    return HttpResponse("<h1>About Page</h1>")


def contact_view(request):
    return HttpResponse("<h1>Contact Page</h1>")
