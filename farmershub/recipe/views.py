from django.shortcuts import render
from .models import *

# Create your views here.
def recipe(request):
  recipe=Recipe.objects.all()
  incredient=RecipeIngredient.objects.all()
  context={
    "recipe":recipe,
    "incredient":incredient
  }
  return render(request,'recipe/home.html',context)