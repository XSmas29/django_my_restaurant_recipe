from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class RecipeListCreate(generics.ListCreateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer

class IngredientListCreate(generics.ListCreateAPIView):
  queryset = Ingredient.objects.all()
  serializer_class = IngredientSerializer

class IngredientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Ingredient.objects.all()
  serializer_class = IngredientSerializer

class CategoryListCreate(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer