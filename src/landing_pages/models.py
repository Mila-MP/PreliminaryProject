from django.db import models
from django.contrib.auth.models import User


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    machine = models.ForeignKey("Machines", on_delete=models.SET(None), null=True, default=None)
    machine_duration = models.DurationField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return self.recipe_name
    

    
class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=500)
    stock_quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name
    

    
class Recipes_Ingredients(models.Model):
    recipe = models.ForeignKey("Recipes", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredients", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ["recipe", "ingredient"]

    def __str__(self):
        return f"{self.quantity} {self.ingredient.unit} of {self.ingredient.ingredient_name} in {self.recipe.recipe_name}"
    

    
class Machines(models.Model):
    # Tuple contains value stored in database and human-readable name
    status_choices = [("In use", "In use"), ("Free", "Free")]

    machine_name = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status_choices, default="Free")
    remaining_time = models.FloatField(default=0.0)
    last_used = models.DateTimeField(null=True, blank=True)
    machine_type = models.CharField(max_length=500)

    def __str__(self):
        return self.machine_name


    
class Recipe_Log(models.Model):
    recipe = models.ForeignKey("Recipes", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)



class Products(models.Model):
    status_choices = [("Fresh", "Fresh"), ("Expired", "Expired")]
    recipe = models.ForeignKey("Recipes", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=status_choices, default="Fresh")

