from django.urls import path
from . import views

urlpatterns = [
    path("machine_not_free/", views.make_recipe, name="machine_not_free"),
    path("make_recipe/<int:recipe_id>/", views.make_recipe, name="make_recipe"),
]