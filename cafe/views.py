from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cafe.models import Product, Order, FeedBack
from cafe.permissions import IsAdminOrAuthenticatedReadOnly
from cafe.serializers import (
    ProductRetrieveCreateSerializer,
    ProductListSerializer,
    OrderListRetrieveSerializer,
    OrderCreateSerializer,
    FeedBackListSerializer,
    FeedBackCreateSerializer
)
from cafe.email_messages import send_mail


class ProductView(ModelViewSet):
    serializer_class = ProductRetrieveCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_serializer_class(self):
        serializer = ProductRetrieveCreateSerializer
        if self.action == "list":
            serializer = ProductListSerializer
        return serializer

    def get_queryset(self):
        queryset = self.queryset
        for param in self.request.query_params:
            queryset = queryset.filter(product_type__iexact=param)

        return queryset


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

    def post(self, request, *args, **kwargs):
        products_ids = [int(i) for i in request.data.getlist("products")]
        products = Product.objects.filter(id__in=products_ids)
        product_names = [product.title for product in products]
        message = f"Your order contains the following products: {', '.join(product_names)}"
        send_mail(self.request.user.email, message, request.data["takeaway"])
        return self.create(request, *args, **kwargs)


class FeedBackView(GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin
                   ):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = FeedBack.objects.all()
        if self.request.user.is_staff:
            return queryset
        if self.request.method == "GET" and "pk" in self.kwargs:
            queryset = queryset.filter(user=self.request.user)

        return queryset

    def get_serializer_class(self):
        serializer = FeedBackListSerializer
        if self.request.method in ["POST", "PUT", "PATCH"]:
            serializer = FeedBackCreateSerializer
        return serializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
