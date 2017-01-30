from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from quickstart.models import User, ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer
from quickstart.serializers import UserSerializer, PaymentTypeSerializer, GroupSerializer, ProductSerializer, BangOrderSerializer, OrderHasProductsSerializer, ProductTypeSerializer, CustomerSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing user instances.
    author: Ali Kimbrell
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing group instances.
    author: Whitney Cormack
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductViewSet(viewsets.ModelViewSet):
	"""
    A ViewSet for viewing and editing product instances.
    author: Trent Hand
	"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class BangOrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = BangOrder.objects.all()
    serializer_class = BangOrderSerializer

class OrderHasProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = OrderHasProducts.objects.all()
    serializer_class = OrderHasProductsSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
















