from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangapi.models import ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.Customer`
    author: Mark Ellis
    """
    class Meta:
        model = Customer
        fields = ('url', 'user', 'address', 'city', 'state_province', 'country', 'payment_type',  )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Ali Kimbrell
    """
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'groups', )

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`auth.User`
    author: Ali Kimbrell
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :models:`bangapi.Group`
    author: Richie Van Sickle
    """
    class Meta:
        model = Group
        fields = ('url', 'name')

class BangOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.BangOrder`
    author: Richie Van Sickle
    """
    class Meta:
        model = BangOrder
        fields = ('status', 'user', 'payment_type')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.ProductType`
    author: Richie Van Sickle
    """
    class Meta:
        model = ProductType
        fields = ('name',)

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :models:`bangapi.PaymentType`
    author: Richie Van Sickle
    """
    class Meta:
        model = PaymentType
        fields = ('type_name', 'account_number',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.Product`
    author: Richie Van Sickle
    """
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product_type', 'user')

class OrderHasProductsSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related
    to :model:`bangapi.OrderHasProducts`
    author: Richie Van Sickle
    """
    class Meta:
        model = OrderHasProducts
        fields = ('order', 'product')






