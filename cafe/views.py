from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cafe.models import Product, Order, FeedBack
from cafe.permissions import IsAdminOrReadOnly
from cafe.serializers import (
    ProductRetrieveCreateSerializer,
    ProductListSerializer,
    OrderListRetrieveSerializer, OrderCreateSerializer, FeedBackListSerializer, FeedBackCreateSerializer
)


class ProductView(ModelViewSet):
    serializer_class = ProductRetrieveCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        serializer = ProductRetrieveCreateSerializer
        if self.action == "list":
            serializer = ProductListSerializer
        return serializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer = OrderListRetrieveSerializer
        if self.request.method == "POST":
            serializer = OrderCreateSerializer

        return serializer

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset


class FeedBackView(GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin
                   ):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackListSerializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            self.queryset = FeedBack.objects.filter(user=request.user)
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = FeedBackCreateSerializer
        return self.create(request, *args, **kwargs)
