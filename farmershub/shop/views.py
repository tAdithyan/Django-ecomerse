from django.shortcuts import render

# Create your views here.
def shop(request):
  return render(request,'shop/shop.html')
def login(request):
  return render(request,'login_signup/login/login.html')