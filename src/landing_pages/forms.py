from django import forms
from .models import Recipes, Machines, Ingredients, Recipes_Ingredients

class RecipesModelForm(forms.ModelForm):
    machine_duration = forms.DurationField(
        required=False,
        help_text="Enter duration in seconds (e.g. 30 for 30 seconds)",
        widget=forms.NumberInput(attrs={'step': 'any'}),
    )
    class Meta:
        model = Recipes
        fields = ["recipe_name", "machine", "machine_duration"]
        labels = {
            "recipe_name": "Recipe",
            "machine": "Machine",
            "machine_duration": "Duration"
        }

class MachinesModelForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = ["machine_name", "machine_type"]


class IngredientsModelForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ["ingredient_name", "stock_quantity", "unit"]
        labels = {
            "ingredient_name": "Ingredient",
            "stock_quantity": "Quantity",
            "unit": "Unit"
        }

class RecipesIngredientsModelForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all())
    class Meta:
        model = Recipes_Ingredients
        fields = ["ingredient", "quantity"]
