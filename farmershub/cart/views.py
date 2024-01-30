from django.shortcuts import render
from shop.models import *
# Create your views here.
def cart(request):
 product=Product.objects.filter()
 return render(request,'cart/cart.html',{'product':product})


def cart_add(request):
  pass

def cart_delete(request):
  pass

def cart_update(request):
  pass