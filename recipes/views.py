from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

# from utils.recipes.factory import make_recipe


def recipes_home_page(request):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
        ).order_by("-id")
    )
    context = {"recipes": recipes}

    return render(request, "recipes/pages/home.html", context=context)


def recipe_page(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    context = {"is_detail_page": True, "recipe": recipe, "title": f"{recipe.title} | "}

    return render(request, "recipes/pages/recipe-detail.html", context=context)


def category_page(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )
    context = {"recipes": recipes, "title": f"{recipes[0].category.name} | "}

    return render(request, "recipes/pages/category.html", context=context)
