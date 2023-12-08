from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .tasks import reset_machine_status
from landing_pages.models import Recipes, Recipes_Ingredients, Recipe_Log, Products

@login_required(login_url="/login")
def make_recipe(request, recipe_id):

    if request.method == "POST":
        recipe = get_object_or_404(Recipes, id=recipe_id)
        machine = recipe.machine # Machine associated with the given recipe
        recipe_duration = recipe.machine_duration

        if machine == None:
            return redirect("home_page")
        
        else:
            if machine.status == "Free":
                # Update machine status to "In use"
                machine.status = "In use"
                machine.last_used = timezone.now()
                machine.save()

                # Status will be reset to free once the recipe is completed
                reset_machine_status.apply_async((machine.id,),countdown = recipe_duration.total_seconds())

                # Get the ingredients needed for the recipe
                recipe_ingredients = Recipes_Ingredients.objects.filter(recipe=recipe)

                # Update the Ingredients table based on the recipe
                for recipe_ingredient in recipe_ingredients:
                    ingredient = recipe_ingredient.ingredient
                    new_quantity = ingredient.stock_quantity - recipe_ingredient.quantity
                    ingredient.stock_quantity = max(0, new_quantity)
                    ingredient.save()

                # Create a log entry for the recipe
                recipe_log = Recipe_Log.objects.create(recipe=recipe)
                # Add to product inventory
                product = Products.objects.create(recipe=recipe, expiry_date=timezone.now())
                return redirect("home_page")

            # If machine is not free
            else:
                remaining_time = recipe_duration - (timezone.now()-machine.last_used)
                context = {
                    "recipe": recipe,
                    "remaining_time": remaining_time
                }
                return render(request, "baking/machine_not_free.html", context)
        
    return redirect('home_page') 
