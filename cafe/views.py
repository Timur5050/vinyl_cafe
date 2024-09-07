from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from cafe.models import Product, Order
from cafe.permissions import IsAdminOrReadOnly
from cafe.serializers import (
    ProductRetrieveCreateSerializer,
    ProductListSerializer,
    OrderListRetrieveSerializer, OrderCreateSerializer
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
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        serializer = OrderListRetrieveSerializer
        if self.request.method == "POST":
            serializer = OrderCreateSerializer

        return serializer

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset

