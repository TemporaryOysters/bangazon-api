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

	def __str__(self):
		return 'You can purchase this %s, described: %s. The price is $%s' % (self.name, self.description, self.price)

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

# This class extends the User class to include necessary fields
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=240)
	city = models.CharField(max_length=55)
	state_province = models.CharField(max_length=55)
	country = models.CharField(max_length=55)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)