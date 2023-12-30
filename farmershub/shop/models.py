from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100,null=True,unique=True)
    categoryname=models.CharField(max_length=100,null=True,unique=True)
    image=models.ImageField(upload_to='category', null=True)



    def __str__(self) -> str:
     return self.title
    
class latestProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    Currentprice = models.DecimalField(max_digits=10, decimal_places=2)
    Oldprice=models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Discount=models.IntegerField()
    image=models.ImageField(upload_to='newproducts', null=True)



    def __str__(self):
        return self.name

    

class banner_area(models.Model):
   image=models.ImageField(upload_to='banner', null=True)
   title=models.CharField(max_length=100,default="" ,null=True)
   deal=models.CharField(max_length=50,default="",null=True)
   sale=models.IntegerField(null=True)
   discount=models.IntegerField(null=True)
   link=models.CharField(max_length=100,default="",null=True,blank=True)
   def __str__(self) -> str:
     return self.title
    