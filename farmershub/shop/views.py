from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages



# Create your views here.
def shop(request):
  Catagory=Category.objects.all()
  Latestproducts=latestProducts.objects.all()
  product=Product.objects.all()



  banner=banner_area.objects.all()
  context={
    'banner':banner,
    'Catagory':Catagory,
    'Latestproducts':Latestproducts,
     'product':product
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



def productsiteams(request,slug):
  
  if(Category.objects.filter( slug=slug)):
    product=Product.objects.filter(category__slug=slug)
    category_name=Category.objects.filter(slug=slug).first()
   
    context={
           'product':product,
            'category_name':category_name
 }


    return render(request,'shop/product.html',context)

  else:
      messages.warning(request,"no such category")
      return redirect(shop)

def products(request):
   product=Product.objects.all()
   productiteam={
     'product':product
   }
   return render(request,'shop/Allproduct.html',productiteam)



def search(request):
  q=request.GET['q']
  product=Product.objects.filter(name__icontains=q).order_by('-id')
  return render(request,'shop/Allproduct.html',{'product':product})
