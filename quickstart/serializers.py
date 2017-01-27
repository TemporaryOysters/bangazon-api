from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import ProductType, Product, PaymentType, BangOrder, OrderHasProducts

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BangOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BangOrder
        fields = ('status', 'user', 'payment_type')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('name',)

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('type_name', 'account_number',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'product_type', 'user')

class OrderHasProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderHasProducts
        fields = ('order', 'product')






