from django.db import models
from django.contrib.auth.models import User

    

    




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
    is_featured = models.BooleanField(default=False,null=True)
    is_Dealsoftheday=models.BooleanField(default=False,null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Profile(models.Model):
        user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
        username=models.CharField(null=True,max_length=225)
        bio=models.TextField()
        image=models.ImageField(upload_to='newproducts', null=True)

        def __str__(self):
            return str(self.user)
