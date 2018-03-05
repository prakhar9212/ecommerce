from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token , verify_jwt_token, refresh_jwt_token
# from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products$', views.products, name='products'),

    url(r'^products/(?P<pk>[0-9]+)/$', views.productDetail, name = 'productDetail'),
    url(r'^products/create/$', views.ProductCreate.as_view(), name = 'productCreate'),
    url(r'^products/(?P<pk>[0-9]+)/update/$', views.ProductUpdate.as_view(), name = 'productUpdate'),
    url(r'^products/(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name = 'productDelete'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^subcatagory/$', views.SubcatagoryCreate.as_view(), name='SubcatagoryCreate'),

    url(r'^orders/$', views.orders, name='orders'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderUpdate.as_view(), name = 'orderUpdate'),
    url(r'^orders/(?P<pk>[0-9]+)/delete/$', views.OrderDelete.as_view(), name = 'orderDelete'),
    url(r'^buyers/$', views.BuyerList.as_view(), name='buyers'),
    url(r'^buyers/(?P<pk>[0-9]+)/$', views.BuyerDetail.as_view(), name='buyersDetail'),






    url(r'^api/api-token-auth/', obtain_jwt_token),
    url(r'^api/api-token-verify/', verify_jwt_token),
    url(r'^api/api-token-refresh/', refresh_jwt_token),


]


urlpatterns += [
    url(r'^api/api-token-auth/', obtain_jwt_token)
]