from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from quickstart.models import User, ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer
from quickstart.serializers import UserSerializer, PaymentTypeSerializer, GroupSerializer, ProductSerializer, BangOrderSerializer, OrderHasProductsSerializer, ProductTypeSerializer, CustomerSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
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
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows products to be viewed or edited.
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
















