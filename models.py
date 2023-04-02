from django.db import models

# Create your models here means table that we need to run in other fiels.

class product(models.Model):
    product_name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    subcategory=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=400)
    image=models.ImageField(upload_to='images/images')

class contacts(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=200)

