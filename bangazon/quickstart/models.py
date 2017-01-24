from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=55)
	last_name = models.CharField(max_length=55)
	street_address = models.CharField(max_length=55)
	city = models.CharField(max_length=55)
	state_province = models.CharField(max_length=15)

class Product(models.Model):
	name = models.CharField(max_length=55)
	description = models.CharField(max_length=240)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	product_typeId = models.ForeignKey(ProductType, on_delete=models.Cascade)
	customerId = models.ForeignKey(Customer, on_delete=models.Cascade)

class ProductType(models.Model):
	name = models.CharField(max_length=55)

class Orders(models.Model):
	productId = models.ForeignKey(Product, on_delete=models.Cascade)
	customerId = models.ForeignKey(Customer, on_delete=models.Cascade)
	payment_typeId = models.ForeignKey(PaymentType, on_delete=models.Cascade)

class PaymentType(models.Model):
	type_name = models.CharField(max_length=55)
	account_number = models.IntegerField()

class CustomerHasPaymentTypes(models.Model):
	customerId = models.ManyToManyField(Customer)
	payment_typeId = models.ManyToManyField(PaymentType)
