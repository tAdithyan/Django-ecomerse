from django.shortcuts import render
from shop.models import *
from django.contrib import messages

# Create your views here.
def cart(request):
 product=Product.objects.filter()
 
 return render(request,'cart/cart.html',{'product':product})


def orderconfir(request):
  return render(request,'cart/orderconfirmation.html')
def payment(request):
  return render(request,'payment/payment.html')
def delivary(request):
  return render(request,'delivary/delivary.html')

