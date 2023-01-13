from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('products/<str:cat>',views.products,name='products'),
    path('recipes/',views.recipes,name='recipes'),
    path('showrecipe/<int:dataid>',views.showrecipe,name='showrecipe'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('register',views.register,name='register'),
    path('regdata',views.regdata,name='regdata'),
    path('logindata',views.logindata,name='logindata'),
    path('logout',views.logout,name='logout'),
    path('cart1/<int:prodid>',views.cart1,name='cart1'),
    path('mycart/',views.mycart,name='mycart'),
    path('productdetail/<int:dataid>',views.productdetail,name='productdetail'),
    path('deletecart/<int:dataid>',views.deletecart,name='deletecart'),
    path('checkout/',views.checkout,name='checkout'),
    path('orders_db/',views.orders_db,name='orders_db'),
    path('cartupdate/',views.cartupdate,name='cartupdate'),
    path('reset_password',views.reset_password,name='reset_password'),
    path('password',views.password,name='password'),
    path('passwordform',views.passwordform,name='passwordform'),
    path('pricerange/',views.pricerange,name='pricerange'),
    path('contact/', views.contact, name='contact'),
    path('contactdata/', views.contactdata, name='contactdata')
]