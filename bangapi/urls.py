from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bangapi import views

urlpatterns = [
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # url(r'^$', views.index, name='index'),
    # url(r'^login$', views.LoginView.as_view(), name='login'),
    # url(r'^register$', views.register_user, name='register_user'),
]

urlpatterns = format_suffix_patterns(urlpatterns)