from django.db import models

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
     return self.title
    

class banner_area(models.Model):
   image=models.ImageField(upload_to='banner')
   title=models.CharField(max_length=100,default="")
   deal=models.CharField(max_length=50,default="")
   sale=models.IntegerField()
   discount=models.IntegerField()
   link=models.CharField(max_length=100,default="")
   def __str__(self) -> str:
     return self.title
    