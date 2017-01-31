from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from bangapi.models import User, ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer
from bangapi.serializers import UserSerializer, PaymentTypeSerializer, GroupSerializer, ProductSerializer, BangOrderSerializer, OrderHasProductsSerializer, ProductTypeSerializer, CustomerSerializer, ClientSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing user instances.
    author: Ali Kimbrell
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            serializer_class = UserSerializer
            return serializer_class
        else:
            serializer_class = ClientSerializer
            return serializer_class

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    author: Mark Ellis
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
    author: Richie VanSickle
    """
    queryset = BangOrder.objects.all()
    serializer_class = BangOrderSerializer

class OrderHasProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    author: Ali Kimbrell
    """
    queryset = OrderHasProducts.objects.all()
    serializer_class = OrderHasProductsSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    author: Whitney Cormack
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    author: Trent Hand
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
















