from django.db import models
from django.contrib.auth.models import User

class ProductType(models.Model):
	name = models.CharField(max_length=55)

class Product(models.Model):
	name = models.CharField(max_length=55)
	description = models.CharField(max_length=240)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class PaymentType(models.Model):
	type_name = models.CharField(max_length=55)
	account_number = models.IntegerField()

class BangOrder(models.Model):
	status = models.CharField(max_length=55)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

class OrderHasProducts(models.Model):
	order = models.ForeignKey(BangOrder, default=1, null=True)
	product = models.ForeignKey(Product, default=1, null=True)