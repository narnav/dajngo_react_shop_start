from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()


class Pita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # friend = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()



class Category(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    desc = models.TextField()

class Products(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    category =models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    price =models.SmallIntegerField()
    desc = models.TextField()
