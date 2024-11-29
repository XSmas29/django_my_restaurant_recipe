from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
  # return HttpResponse('Hello, Django!')
  return redirect('recipes')

def recipes(request):
  return render(request, 'recipes.html')

def ingredients(request):
  return render(request, 'ingredients.html')

def categories(request):
  return render(request, 'categories.html')