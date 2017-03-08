from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from bangapi.models import User, ProductType, Product, PaymentType, BangOrder, OrderHasProducts, Customer
from bangapi.serializers import UserSerializer, PaymentTypeSerializer, GroupSerializer, ProductSerializer, BangOrderSerializer, OrderHasProductsSerializer, ProductTypeSerializer, CustomerSerializer




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


def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    # Commit the user to the database by saving it
    new_user.save()

    return login_user(request)

class LoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        })

    @csrf_exempt
    def post(self,request):
        permission_classes = (AllowAny,)

        req_body = json.loads(request.body.decode())
        username = req_body['username']
        password = req_body['password']
        user = authenticate(username=username, password=password)

        success = False
        if user is not None:
            if user.is_active:
                login(request, user)
                data = json.dumps({
                    'success': True,
                    'username': user.username,
                    'email': user.email,
                })
                return HttpResponse(data, content_type='application/json')

            return HttpResponse(self._error_response('disabled'), content_type='application/json')
        return HttpResponse(self._error_response('invalid'), content_type='application/json')














