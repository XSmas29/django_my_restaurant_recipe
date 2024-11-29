from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse('Hello, Django!')
  return render(request, 'home.html')

def recipes(request):
  return HttpResponse('Recipes')

def ingredients(request):
  return HttpResponse('Ingredients')

def categories(request):
  return HttpResponse('Categories')