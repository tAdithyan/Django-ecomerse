from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



# Create your views here.
def shop(request):
  Catagory=Category.objects.all()
  # Latestproducts=latestProducts.objects.all()
  product=Product.objects.all()
  featured_products = Product.objects.filter(is_featured=True)
  Deals=Product.objects.filter(is_Dealsoftheday=True)





  
  context={
    'Catagory':Catagory,
    'featured_products':featured_products,
     'product':product,
     'Deals':Deals
  }
  return render(request,'shop/shop2.html',context)
def log_in(request):
 if request.method=="POST":


  email=request.POST.get('email')

  password=request.POST.get('password')

  user =authenticate(request, username=email, password=password)
  
  
  if user:
     login(request,user)
     return redirect('shop')



  else:
    messages.error(request,"invalid user name")
 
 

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
  query=request.GET['q']
  if query:
   product=Product.objects.filter(name__icontains=query).order_by('-id')
 
  
  
  
  if ( query==""):
          return redirect(shop)



  return render(request,'shop/Allproduct.html',{'product':product})
def user_is_superuser(user):
    
    return user.is_authenticated and user.is_superuser







def content(request,id):
  blog=Product.objects.get(id=id)


  contexnt={
               'blog':blog,
               'login_error_message': "You need to login to add this product to the cart."
  }
 

            

    
     
  
  return render(request,'shop/contentpage.html',contexnt)

def addproduct(request):
   if request.method=='POST':
       form=additeam(request.POST,request.FILES)
       if form.is_valid():
         form.save()
         return redirect(shop)
   else:  
          form=additeam()
   return render(request,'shop/addproduct.html',{'form':form})
def editproduct(request,id):
     
      blog=Product.objects.get(id=id)
     
  
      if request.method=='POST':
       form=additeam(request.POST or None,request.FILES or None,instance=blog,)
      
       if form.is_valid():
           form.save()
           return redirect(products)
      else:
          form=additeam(instance=blog)

       

      return render(request,'shop/addproduct.html',{'form':form})
def addcategoryiteam(request):
     if request.method=='POST':
         form=addcategory(request.POST,request.FILES)
         if form.is_valid():
          form.save()
          return redirect(shop)
     else:  
            form=addcategory()
     return render(request,'shop/addproduct.html',{'form':form})

def editcategory(request,id):
     
      blog=Category.objects.get(id=id)
  
      if request.method=='POST':
       form=addcategory(request.POST,instance=blog)
       if form.is_valid():
           form.save()
           return redirect(shop)
      else:
          form=addcategory(instance=blog)



      return render(request,'shop/addproduct.html',{'form':form})    
# def deleteproduct(request,id):
#          blog=Product.objects.get(id=id)
#          if request.method=='POST':
#           blog.delete()
#           return redirect(products)
#          return render(request,'shop/delete.html',{'blog':blog})
def deletecategory(request,id):
         blog=Category.objects.get(id=id)
         if request.method=='POST':
          blog.delete()
          return redirect(shop)
         return render(request,'shop/delete.html',{'blog':blog})
def deleteproduct(request,id):
         blog=Product.objects.get(id=id)
         if request.method=='POST':
          blog.delete()
          return redirect(shop)
         return render(request,'shop/delete.html',{'blog':blog})
@login_required
def addToCart(request,id):
   
   email=request.GET.get('productQuantity')
   print(email)
   print('Product Id :',id)


   return redirect(shop)
   
