from django.db import models

# Create your models here.
class admins_db(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='adminimage/',)

    def __str__(self):
        return self.name
#class dummy_db(models.Model):
 #   userid=models.ForeignKey(admins_db,on_delete=models.CASCADE)
  #  adminage=models.CharField(max_length=20)

class products_db(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    categ=models.CharField(max_length=10,null=True,blank=True)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='productimage/')

class recipie_db(models.Model):
    recipiename = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=50)
    instructions = models.TextField(max_length=50)
    image = models.ImageField(upload_to='recipieimage/')

class category_db(models.Model):
    cname = models.CharField(max_length=50,null=True,blank=False)
    catdescpn = models.TextField(max_length=50,null=True,blank=False)
    image = models.ImageField(upload_to='catimage/')