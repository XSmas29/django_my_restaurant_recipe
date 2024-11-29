from django.urls import path
from . import views

urlpatterns = [
  path('/recipes', views.RecipeListCreate.as_view(), name='recipe_list'),
  path('/recipes/<int:pk>', views.RecipeRetrieveUpdateDestroy.as_view(), name='recipe_detail'),
  path('/ingredients', views.IngredientListCreate.as_view(), name='ingredient_list'),
  path('/ingredients/<int:pk>', views.IngredientRetrieveUpdateDestroy.as_view(), name='ingredient_detail'),
  path('/categories', views.CategoryListCreate.as_view(), name='category_list'),
  path('/categories/<int:pk>', views.CategoryRetrieveUpdateDestroy.as_view(), name='category_detail'),
]