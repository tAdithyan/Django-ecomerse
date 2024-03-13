
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def blog(request):
  blog=Blog.objects.all()
  popular=Blog.objects.filter(is_popular=True)
  context={
  "blog":blog,
  "popular":popular,
 }

  return render(request,'blog/blog.html',context)

def addblogs(request):
   if request.method=='POST':
       form=addblog(request.POST,request.FILES)
       if form.is_valid():
         form.save()
         return redirect(blog)
   else:  
          form=addblog()
  
   return render(request,'shop/addproduct.html',{'form':form})

def deleteblog(request,id):
         blogiteam=Blog.objects.get(id=id)
         if request.method=='POST':
          blogiteam.delete()
          return redirect(blog)
         return render(request,'shop/delete.html',{'blogiteam':blogiteam})

def editblog(request,id):
     
      blogs=Blog.objects.get(id=id)
  
      if request.method=='POST':
       form=addblog(request.POST,request.FILES,instance=blogs)
       if form.is_valid():
           form.save()
           return redirect(blog)
      else:
          form=addblog(instance=blogs)



      return render(request,'shop/addproduct.html',{'form':form})
    
