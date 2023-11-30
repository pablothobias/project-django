from django.urls import path
from recipes import views

# or
# from . import views

urlpatterns = [
    path("", views.recipes_home_page),
    path("<int:id>/", views.recipe_page),
]
