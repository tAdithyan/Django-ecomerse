from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100,null=True,unique=True)
    categoryname=models.CharField(max_length=100,null=True,unique=True)
    image=models.ImageField(upload_to='category', null=True)



    def __str__(self) -> str:
     return self.title
    

class banner_area(models.Model):
   image=models.ImageField(upload_to='banner', null=True)
   title=models.CharField(max_length=100,default="" ,null=True)
   deal=models.CharField(max_length=50,default="",null=True)
   sale=models.IntegerField(null=True)
   discount=models.IntegerField(null=True)
   link=models.CharField(max_length=100,default="",null=True,blank=True)
   def __str__(self) -> str:
     return self.title
    