from django.shortcuts import render
from Blog.models import *

# Create your views here.
def homepage(request):
  return render(request,'home/home.html')
