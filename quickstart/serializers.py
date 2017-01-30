from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.Customer model.
    author: Mark Ellis
    """
    class Meta:
        model = Customer
        fields = ('url', 'user', 'address', 'city', 'state_province', 'country', 'payment_type',  )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the auth.models.User model.
    author: Ali Kimbrell
    """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.Group model.
    author: Richie Van Sickle
    """
    class Meta:
        model = Group
        fields = ('url', 'name')

class BangOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.BangOrder model.
    author: Richie Van Sickle
    """
    class Meta:
        model = BangOrder
        fields = ('status', 'user', 'payment_type')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.ProductType model.
    author: Richie Van Sickle
    """
    class Meta:
        model = ProductType
        fields = ('name',)

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.PaymentType model.
    author: Richie Van Sickle
    """
        class Meta:
        model = PaymentType
        fields = ('type_name', 'account_number',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.Product model.
    author: Richie Van Sickle
    """
        class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product_type', 'user')

class OrderHasProductsSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class defines the fields that get serialized/deserialized, related to the models.OrderHasProducts model.
    author: Richie Van Sickle
    """
        class Meta:
        model = OrderHasProducts
        fields = ('order', 'product')






