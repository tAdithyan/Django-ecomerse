from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.shop,name='shop'),
    path('login/',views.login,name='login')
    
  
]
