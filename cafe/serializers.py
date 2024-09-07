from rest_framework import serializers

from cafe.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "product_type",
            "price",
            "available",
            "image",
            "season_product"
        )


class ProductRetrieveCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "product_type",
            "price",
            "available",
            "image",
            "season_product"
        )
