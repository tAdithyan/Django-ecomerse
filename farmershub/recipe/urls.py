from django.contrib import admin
from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('',views.recipe,name='recipe'),
    path('content/<int:id>',views.content,name="content"),
    path('search/',views.searchRecipe,name='searchRecipe'),
    path('addrecipe/',views.addrecipe,name='addrecipe'),
    path('editrecipes/<str:id>',views.editrecipes,name='editrecipes'),
    path('deleterecipe/<int:id>',views.deleterecipes,name='deletrecipes'),



  
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
