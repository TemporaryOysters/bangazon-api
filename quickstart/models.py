from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	street_address = models.CharField(max_length=55)
	city = models.CharField(max_length=55)
	state_province = models.CharField(max_length=15)
	country = models.CharField(max_length=55)
	sign_up_date = models.DateField('sign up date')

class ProductType(models.Model):
	name = models.CharField(max_length=55)

class Product(models.Model):
	name = models.CharField(max_length=55)
	description = models.CharField(max_length=240)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class PaymentType(models.Model):
	type_name = models.CharField(max_length=55)
	account_number = models.IntegerField()

class BangOrder(models.Model):
	status = models.CharField(max_length=55)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

class OrderHasProducts(models.Model):
	orderId = models.ManyToManyField(BangOrder)
	productId = models.ManyToManyField(Product)


