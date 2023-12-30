from django.contrib import admin
from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('',views.shop,name='shop'),
    path('login/',views.log_in,name='login'),
    path('signup/',views.sign_up,name="signup"),
    path('logout/',views.log_out,name='logout')


    
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
