from django.db import models

# Create your models here.
class Ingredient(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=25)
  
  class Meta:
    db_table = 'ingredients'

  def __str__(self):
    return self.name

class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=25)

  class Meta:
    db_table = 'categories'

  def __str__(self):
    return self.name

class Recipe(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=25)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
  ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

  class Meta:
    db_table = 'recipes'

  def __str__(self):
    return self.name