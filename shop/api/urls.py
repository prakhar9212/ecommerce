from django.conf.urls import url, include
from rest_framework import routers
from .views import (
    ProductListAPIView,
    ProductDetailAPIView ,
    ProductUpdateAPIView ,
    ProductDeleteAPIView ,
    ProductCreateAPIView,
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView,
    OrderCreateAPIView,
)



urlpatterns = [
    url(r'^$', ProductListAPIView.as_view(), name='productList'),
    url(r'^create/$', ProductCreateAPIView.as_view(), name='productCreate'),
    url(r'^order/$', OrderCreateAPIView.as_view(), name='orderCreate'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^buyer/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name = 'userDetail'),
    url(r'^(?P<product_id>[0-9]+)/$', ProductDetailAPIView.as_view(), name = 'productDetail'),
    url(r'^(?P<product_id>[0-9]+)/update/$', ProductUpdateAPIView.as_view(), name = 'productUpdate'),
    url(r'^(?P<product_id>[0-9]+)/delete/$', ProductDeleteAPIView.as_view(), name = 'productDelete'),

]

