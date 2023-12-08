from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "home_page"),
    path("recipes/", views.recipe_page, name = "recipe_page"),
    path("recipes/edit/<int:recipe_id>/", views.edit_recipe, name = "edit_recipe"),
    path("recipes/delete/<int:recipe_id>/", views.delete_recipe, name = "delete_recipe"),
    path("recipes/view/<int:recipe_id>/", views.view_recipe_ingredients, name="view_recipe_ingredients"),
    path("inventory/", views.inventory_page, name = "inventory_page"),
    path("machines/", views.machine_page, name = "machine_page"),
    path("machines/edit/<int:machine_id>/", views.edit_machine, name = "edit_machine"),
    path("machines/delete/<int:machine_id>/", views.delete_machine, name = "delete_machine"),
    path("inventory/edit/<int:ingredient_id>/", views.edit_ingredient, name = "edit_ingredient"),
    path("inventory/delete/<int:ingredient_id>/", views.delete_ingredient, name = "delete_ingredient"),
    path("baking_log/", views.baking_log, name="baking_log"),
]