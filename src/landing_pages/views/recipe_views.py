from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

from ..models import Recipes, Ingredients, Recipes_Ingredients, Machines, Recipe_Log
from ..forms import RecipesModelForm, RecipesIngredientsModelForm

# If not logged in, redirect to /login
@login_required(login_url="/login")
def home_page(request):
    title = "Inventory Tracker Home Page"
    welcome_message = "Welcome to the Inventory Tracker Home Page"
    recipes = Recipes.objects.all()
    machines = Machines.objects.all()
    context = {
        "title" : title,
        "welcome": welcome_message,
        "recipes": recipes,
        "machines": machines,
    }
    return render(request, "landing_pages/home.html", context)



@login_required(login_url="/login")
def recipe_page(request):
    recipes = Recipes.objects.all() # Fetches all the entries in the Recipes table

    if request.method == "POST":
        recipe_form = RecipesModelForm(request.POST) # Creates form instance with the submitted POST data
        ingredients_formset = formset_factory(RecipesIngredientsModelForm, extra=3)

        if recipe_form.is_valid():
            recipe = recipe_form.save()
            formset = ingredients_formset(request.POST)

            if formset.is_valid():
                for form in formset:
                    ingredient = form.cleaned_data.get('ingredient')
                    quantity = form.cleaned_data.get('quantity')
                    Recipes_Ingredients.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity)

                return redirect("recipe_page")
            
            else:
                print(formset.errors)
            

    else:
        recipe_form = RecipesModelForm()
        ingredients_formset = formset_factory(RecipesIngredientsModelForm, extra=3)
        formset = ingredients_formset()

    title = "Recipes"
    context = {
        "recipes" : recipes,
        "recipe_form": recipe_form,
        "formset": formset,
        "title": title
    }

    return render(request, "landing_pages/recipes.html", context)



@login_required(login_url="/login")
def edit_recipe(request, recipe_id):
    # Retrieve the recipe object with the specified recipe_id from the database.
    # If the object does not exist, it returns a 404 page.
    recipe = get_object_or_404(Recipes, id=recipe_id)
    form = RecipesModelForm(instance=recipe)

    # Check if the form is submitted via POST
    if request.method == "POST":
        # Create a form instance with the submitted POST data and the existing recipe data
        form = RecipesModelForm(request.POST, instance=recipe)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to update the existing recipe in the database
            form.save()
            return redirect("recipe_page")

    context = {
        "form": form,
        "title": "Edit Recipe"
    }

    return render(request, "landing_pages/edit_recipe.html", context)


@login_required(login_url="/login")
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)

    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_page")
    
    context = {
        "recipe": recipe,
        "title": "Delete Recipe"
    }

    return render(request, "landing_pages/delete_recipe.html", context)

@login_required(login_url="/login")
def view_recipe_ingredients(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    ingredients = Recipes_Ingredients.objects.filter(recipe=recipe)
    
    context = {
        "recipe": recipe,
        "ingredients": ingredients,
        "title": f"Ingredients for {recipe.recipe_name}"
    }
    return render(request, "landing_pages/view_recipe_ingredients.html", context)

@login_required(login_url="/login")
def baking_log(request):
    logs = Recipe_Log.objects.all()
    title = "Baking Log"
    context = {
        "logs": logs,
        "title": title
    }

    return render(request, "landing_pages/baking_log.html", context)