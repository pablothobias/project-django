from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

from utils.recipes.factory import make_recipe

# Create your views here.


def recipes_home_page(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    context = {"recipes": recipes}
    return render(request, "recipes/pages/home.html", context=context)


def recipe_page(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {"is_detail_page": True, "recipe": recipe}
    return render(request, "recipes/pages/recipe-detail.html", context=context)


def category_page(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by("-id")
    context = {"recipes": recipes}
    return render(request, "recipes/pages/home.html", context=context)
