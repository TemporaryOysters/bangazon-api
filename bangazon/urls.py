from django.conf.urls import url, include
from rest_framework import routers
from bangapi import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.BangOrderViewSet)
router.register(r'products_in_order', views.OrderHasProductsViewSet)
router.register(r'payment_type', views.PaymentTypeViewSet)
router.register(r'product_type', views.ProductTypeViewSet)
router.register(r'customer', views.CustomerViewSet)
# router.register(r'loginview', views.LoginView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^login$', views.LoginView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]