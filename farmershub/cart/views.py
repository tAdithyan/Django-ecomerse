from django.shortcuts import render
from shop.models import *
# Create your views here.
def cart(request):
 product=Product.objects.filter()
 return render(request,'cart/cart.html',{'product':product})


def orderconfir(request):
  return render(request,'cart/orderconfirmation.html')

