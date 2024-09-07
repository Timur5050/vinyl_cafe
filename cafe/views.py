from rest_framework.viewsets import ModelViewSet

from cafe.models import Product
from cafe.permissions import IsAdminOrReadOnly
from cafe.serializers import (
    ProductRetrieveCreateSerializer,
    ProductListSerializer
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
