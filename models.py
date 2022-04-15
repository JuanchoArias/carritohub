from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0)
    direction = models.CharField(max_length=100, null=False, blank=False)
    subtotal = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    send_price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)
    is_buyed = models.BooleanField(default=False)
    buy = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0) 
    
class ProductsNotBuyed(models.Model):
    cart = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
class ProductsBuyed(models.Model):
    cart = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    