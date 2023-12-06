from django.http import Http404
from django.shortcuts import render
from .models import Recipe

from utils.recipes.factory import make_recipe

# Create your views here.


def recipes_home_page(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    if not recipes:
        raise Http404("Recipes not found 😢")

    context = {"recipes": recipes}
    return render(request, "recipes/pages/home.html", context=context)


def recipe_page(request, id):
    recipe = Recipe.objects.get(id=id)

    if not recipe:
        raise Http404("Recipe not found 😢")

    context = {"is_detail_page": True, "recipe": recipe, "title": f"{recipe.title} | "}
    return render(request, "recipes/pages/recipe-detail.html", context=context)


def category_page(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by("-id")

    if not recipes:
        raise Http404("Category not found 😢")

    context = {"recipes": recipes, "title": f"{recipes.first().category.name} | "}
    return render(request, "recipes/pages/category.html", context=context)
