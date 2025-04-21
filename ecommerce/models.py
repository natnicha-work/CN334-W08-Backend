from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default="Unknown")
    address = models.CharField(max_length=500, blank=True)
    tel = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()

class Shipping(models.Model):
    method = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expired = models.CharField(max_length=5)
    card_no = models.CharField(max_length=100)
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=20)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    shipping = models.ForeignKey(Shipping, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()