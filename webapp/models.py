from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from myapp.models import products_db

class regdb(models.Model):
    name=models.CharField(max_length=25,null=True,blank=False)
    mobileno=models.CharField(max_length=25,null=True,blank=False)
    email=models.CharField(max_length=25,null=True,blank=False)
    password=models.CharField(max_length=25,null=True,blank=False)

class Cart(models.Model):
    productid=models.ForeignKey(products_db,on_delete=CASCADE,null=True,blank=True)
    userid=models.ForeignKey(regdb,on_delete=CASCADE,null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)

class orders(models.Model):
    Firstname = models.CharField(max_length=25,null=True,blank=False)
    username = models.CharField(max_length=25,null=True,blank=False)
    email = models.CharField(max_length=25,null=True,blank=False)
    address = models.CharField(max_length=25,null=True,blank=False)
    country = models.CharField(max_length=25,null=True,blank=False)
    state = models.CharField(max_length=25,null=True,blank=False)
    zipcode = models.CharField(max_length=25,null=True,blank=False)
    cartid = models.ForeignKey(Cart,on_delete=CASCADE,null=True,blank=True)

class Contact_db(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=10)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=30)
    