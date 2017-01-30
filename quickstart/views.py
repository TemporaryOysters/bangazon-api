from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from quickstart.models import User, ProductType, Product, PaymentType,
    BangOrder, OrderHasProducts
from quickstart.serializers import UserSerializer, PaymentTypeSerializer,
    GroupSerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing user instances.
    author: Ali Kimbrell
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


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


