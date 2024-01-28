from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_popular=models.BooleanField(default=False,null=True)

   
    upload_date=models.DateTimeField(auto_now_add=True, blank=True)
    
    image=models.ImageField(upload_to='blogs', null=True)


    def __str__(self):
        return self.title