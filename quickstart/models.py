from django.db import models
from django.contrib.auth.models import User

class ProductType(models.Model):
	"""
	Stores a single Product Type
	author: Mark Ellis
	"""
	name = models.CharField(max_length=55)

class Product(models.Model):
	"""
	Stores a single Product, related to :model:`quickstart.ProductType` and
	:model:`auth.User`.
	author: Mark Ellis
	"""
	name = models.CharField(max_length=55)
	description = models.CharField(max_length=240)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return 'You can purchase this %s, described: %s. The price is $%s' % (self.name, self.description, self.price)

class PaymentType(models.Model):
	"""
	Stores a single Payment Type
	author: Mark Ellis
	"""
	type_name = models.CharField(max_length=55)
	account_number = models.IntegerField()

	def __str__(self):
		return '%s' % (self.type_name)

class BangOrder(models.Model):
	"""
	Stores a single BangOrder, related to model:`auth.User` and
	:model:`quickstart.PaymentType`
	author: Mark Ellis
	"""
	status = models.CharField(max_length=55)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

class OrderHasProducts(models.Model):
	"""
	Stores a single instance of relationship between
	:model:`quickstart.BangOrder` and :model:`quickstart.Product`
	author: Mark Ellis
	"""
	order = models.ForeignKey(BangOrder, default=1, null=True)
	product = models.ForeignKey(Product, default=1, null=True)

class Customer(models.Model):
	"""
	Extends :model:`auth.User`
	author: Mark Ellis
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=240)
	city = models.CharField(max_length=55)
	state_province = models.CharField(max_length=55)
	country = models.CharField(max_length=55)
	payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

