from django.contrib import admin
from django.urls import path,include
from .import views
# from myapp.appapi import product_create_list,product_details

#import myapp

urlpatterns = [
    path('base/', views.my,name='my'),
    path('addproduct/', views.addproduct,name='addproduct'),
    path('productdatas/', views.productdatas,name='productdatas'),
    path('viewproducts/', views.viewproducts,name='viewproducts'),
    path('deleteproducts/', views.deleteproducts,name='deleteproducts'),
    path('editproducts/<int:dataid>',views.editproducts,name='editproducts'),
    path('updateproducts/<int:dataid>',views.updateproducts,name='updateproducts'),
    path('addrecipies/', views.addrecipies,name='addrecipies'),
    path('viewrecipies/', views.viewrecipies,name='viewrecipies'),
    path('recipiedatas/', views.recipiedatas,name='recipiedatas'),
    path('deleterecipies/', views.deleterecipies,name='deleterecipies'),
    path('editrecipies/<int:dataid>',views.editrecipies,name='editrecipies'),
    path('updaterecipies/<int:dataid>',views.updaterecipies,name='updaterecipies'),
    path('customers/', views.customers,name='customers'),
    path('order/', views.order,name='order'),
    path('cart/', views.cart, name='cart'),
    path('message/', views.message, name='message'),
    path('categorydescription/', views.categorydescription,name='categorydescription'),
    path('categorydatas/', views.categorydatas,name='categorydatas'),
    path('viewcategory/', views.viewcategory,name='viewcategory'),
    path('deletecategory/<int:dataid>', views.deletecategory,name='deletecategory'),
    path('editcategory/<int:dataid>',views.editcategory,name='editcategory'),
    path('updatecategory/<int:dataid>',views.updatecategory,name='updatecategory'),
    path('adminlogin/',views.adminlogin, name='adminlogin'),
    path('adlogin/', views.adlogin, name='adlogin'),
    path('adlogout/',views.adlogout,name='adlogout')
]