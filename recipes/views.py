from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def recipes_home_page(request):
    return render(request, "recipes/pages/home.html")


def recipe_page(request, id):
    return render(request, "recipes/pages/home.html", context=context)
