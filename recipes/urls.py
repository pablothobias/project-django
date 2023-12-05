from django.urls import path
from recipes import views

# or
# from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.recipes_home_page, name="home"),
    path("recipes/<int:id>/", views.recipe_page, name="recipe"),
    path("recipes/category/<int:category_id>/", views.category_page, name="category"),
]
