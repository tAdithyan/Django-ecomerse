from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings


def my_view(request):
    dark_mode = request.session.get(settings.DARK_MODE_SESSION_KEY, False)
    return render(request, 'my_template.html', {'dark_mode': dark_mode})

# Create your views here.
def shop(request):
  Catagory=Categories.objects.all()
  Latestproducts=latestProducts.objects.all()


  banner=banner_area.objects.all()
  context={
    'banner':banner,
    'Catagory':Catagory,
    'Latestproducts':Latestproducts
  }
  return render(request,'shop/shop2.html',context)
def log_in(request):
 if request.method=="POST":


  email=request.POST.get('email')

  password=request.POST.get('password')
  user =authenticate(request, username=email, password=password)
  
  
  if user is not None:
     login(request,user)
  else:
     pass
  return redirect("shop")
 

 return render(request,'login_signup/login/login.html')
def sign_up(request):
  if request.method=="POST":

   fname=request.POST.get('name')
   email=request.POST.get('email')

   password=request.POST.get('password')

   user = User.objects.create_user(first_name=fname,username=email,email=email, password=password)
 
   user.save()
   return redirect(log_in)

  return render(request,'login_signup/signup/signup.html')
def log_out(request):
    logout(request)
    return redirect("shop")


# views.py



