from django.db import models

    
class latestProducts(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    Currentprice = models.DecimalField(max_digits=10, decimal_places=2)
    Oldprice=models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    # category = models.ForeignKey(Categories, on_delete=models.CASCADE)
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



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image=models.ImageField(upload_to='category', null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    Currentprice = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    Oldprice=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    Discount=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to='newproducts', null=True)



    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
