from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Ingredients, Products
from ..forms import IngredientsModelForm

@login_required(login_url="/login")
def inventory_page(request):
    # Fetches all the entries in the Ingredients and Products table
    ingredients = Ingredients.objects.all() 
    products = Products.objects.all()

    product_dict = {}

    for product in products:
        if product not in product_dict:
            product_dict.setdefault(product.recipe, 0)
        product_dict[product.recipe] += 1

    if request.method == "POST":
        form = IngredientsModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("inventory_page")
    
    else:
        form = IngredientsModelForm()

    title = "Inventory"
    context = {
        "ingredients" : ingredients,
        "product_dict": product_dict,
        "form": form,
        "title": title
    }

    print(product_dict)

    return render(request, "landing_pages/inventory.html", context)


@login_required(login_url="/login")
def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredients, id=ingredient_id)
    form = IngredientsModelForm(instance=ingredient)

    if request.method == "POST":
        form = IngredientsModelForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect("inventory_page")
        
    context = {
        "form": form,
        "title": "Edit Ingredient"
    }

    return render(request, "landing_pages/edit_ingredient.html", context)

@login_required(login_url="/login")
def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredients, id=ingredient_id)
    if request.method == "POST":
        ingredient.delete()
        return redirect("inventory_page")
    
    context = {
        "ingredient": ingredient,
        "title": "Delete Ingredient"
    }

    return render(request, "landing_pages/delete_ingredient.html", context)