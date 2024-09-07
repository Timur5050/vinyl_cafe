from rest_framework import serializers

from cafe.models import Product, Order


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


class ProductForOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "product_type", "price")


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("products",)

    def create(self, validated_data):
        order = Order.objects.create(user=self.context["request"].user)
        order.product.set(validated_data["products"])
        order.save()
        return order


class OrderListRetrieveSerializer(serializers.ModelSerializer):
    products = ProductForOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ("products", "time")
