from django.db import models

# Create your models here.
class recipeList(models.Model):
    recipeURL = models.CharField(max_length= 255)
    RecipeName = models.CharField(max_length= 255)
    insertDate = models.DateTimeField()

#class addRecipe(models.Model):
#    recipeURL = models.CharField(max_length= 255)
#    recipeName = models.CharField(max_length= 255)
#    insertDate = models.DateTimeField()