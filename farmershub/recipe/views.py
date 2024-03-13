from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def recipe(request):
  recipe=Recipe.objects.all()
  context={
    "recipe":recipe,
  }
  return render(request,'recipe/home.html',context)
def content(request,id):
  blog=Recipe.objects.get(id=id)
  contexnt={
               'blog':blog
  }
 

            

    
     
  
  return render(request,'recipe/recipeiteam.html',contexnt)




def searchRecipe(request):
  query=request.GET['q']
  if query:
   recipe=Recipe.objects.filter(title__icontains=query).order_by('-id')
 
  
  
  
  if ( query==""):
          return redirect(recipe)



  return render(request,'recipe/home.html',{'recipe':recipe})



def addrecipe(request):
   if request.method=='POST':
       form=addrecipes(request.POST,request.FILES)
       if form.is_valid():
         form.save()
         return redirect(recipe)
   else:  
          form=addrecipes()
  
   return render(request,'shop/addproduct.html',{'form':form})

def deleterecipes(request,id):
         blog=Recipe.objects.get(id=id)
         if request.method=='POST':
          blog.delete()
          return redirect(recipe)
         return render(request,'shop/delete.html',{'blog':blog})
def editrecipes(request,id):
     
      blog=Recipe.objects.get(id=id)
  
      if request.method=='POST':
       form=addrecipes(request.POST,instance=blog)
       
       if form.is_valid():
           form.save()
           return redirect(recipe)
      else:
          form=addrecipes(instance=blog)



      return render(request,'shop/addproduct.html',{'form':form})    
    

