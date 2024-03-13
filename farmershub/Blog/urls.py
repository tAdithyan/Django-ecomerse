from django.contrib import admin
from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('',views.blog,name='blog'),
    path('addblogs/',views.addblogs,name='addblogs'),
    path('editblog/<str:id>',views.editblog,name='editblog'),
    path('deleteblog/<int:id>',views.deleteblog,name='deleteblog'),

    



  
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
