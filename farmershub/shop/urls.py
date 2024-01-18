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
    path('content/<str:id>',views.content,name="content"),

    path('category/<str:slug>/', views.productsiteams, name='productsiteams'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('editproduct/<int:id>',views.editproduct,name='editproduct'),
    path('deleteproduct/<int:id>',views.deleteproduct,name='deleteproduct'),


    path('addcategory/',views.addcategoryiteam,name='addcategory'),
    path('editcategory/<int:id>',views.editcategory,name='editcategory'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),



    path('editproduct/<int:id>',views.editproduct,name='editproduct'),

    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
