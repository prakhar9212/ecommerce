from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView ,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                    CreateAPIView,
                                    RetrieveUpdateAPIView,
                                     )
from .serializers import (ProductListSerializer,
                          ProductDetailSerializer ,
                          ProductCreateSerializer,
                          UserCreateSerializer,
                          UserLoginSerializer,
                          UserDetailSerializer,
                          OrderCreateSerializer
                          )
from shop.models import Product , Buyer, Order
from rest_framework.permissions import AllowAny, IsAdminUser , IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class UserCreateAPIView(CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data,status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserDetailAPIView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Buyer.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'







class ProductListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer



class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'product_id'

class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'product_id'
    permission_classes = [IsOwnerOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(seller = self.request.user.seller)

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'product_id'


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(seller = self.request.user.seller, )

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(buyer = self.request.user.buyer )


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserDetailSerializer(user.buyer, context={'request': request}).data
    }