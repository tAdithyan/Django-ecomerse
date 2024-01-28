from django.db import models



# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Ingredient(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.TextField(null=True)
    instructions = models.TextField()
    prep_time = models.IntegerField(null=True)
   
    cook_time = models.IntegerField(null=True)
    image=models.ImageField(upload_to='newproducts', null=True)


    def __str__(self):
        return self.title

# class RecipeIngredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     # ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,null=True)
#     quantity = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.quantity} {self.ingredient.name} for {self.recipe.title}"
