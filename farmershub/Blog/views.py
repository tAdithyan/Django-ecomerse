
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def blog(request):
  blog=Blog.objects.all()

  return render(request,'blog/blog.html',{'blog':blog})