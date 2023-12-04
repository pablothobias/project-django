from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.


def recipes_home_page(request):
    context = {"recipes": [make_recipe() for _ in range(10)]}
    return render(request, "recipes/pages/home.html", context=context)


def recipe_page(request, id):
    context = {"is_detail_page": True, "recipe": make_recipe()}
    return render(request, "recipes/pages/recipe-detail.html", context=context)
