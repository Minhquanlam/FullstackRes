from django.db import models
# Create your models here.
from django.contrib import admin
from django.db.models.fields.related import ForeignKey

# Create your models here.
class pizza(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    price  = models.FloatField(null=False,blank=False)
    protein = models.PositiveIntegerField(null = True, blank= True)
    addictives = models.PositiveIntegerField(null = True, blank= True)
    deco = models.PositiveIntegerField(null = True, blank= True)
    baking =  models.PositiveIntegerField(null = True, blank= True)
    image = models.ImageField()

class drink(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    price  = models.FloatField()
    energy = models.PositiveIntegerField()
    addictives = models.PositiveIntegerField()
    image = models.ImageField(null=True)

class hamburger(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    price  = models.FloatField()
    protein = models.PositiveIntegerField()
    addictives = models.PositiveIntegerField()
    baking =  models.PositiveIntegerField()
    deco = models.PositiveIntegerField()
    image = models.ImageField(null=True) 


class order(models.Model):
    id_order = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_order')
    first_name= models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='0')
    totalcost = models.FloatField(default=0)
    note = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)


