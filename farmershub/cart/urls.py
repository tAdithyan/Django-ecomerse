from django.contrib import admin
from django.urls import path,include
from .  import views
urlpatterns = [
    path('cart/',views.cart,name='cart'),
  
    path('orderconfir/',views.orderconfir,name='orderconfir')

  
]