from django.contrib import admin
from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('',views.shop,name='shop'),
    path('login/',views.log_in,name='login'),
    path('signup/',views.sign_up,name="signup"),
    path('logout/',views.log_out,name='logout'),
    path('products/',views.products,name='products'),
    path('search/',views.search,name='search'),

    path('category/<str:slug>/', views.productsiteams, name='productsiteams'),



    
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
