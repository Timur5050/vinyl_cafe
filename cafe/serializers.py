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
        fields = ("products", "additional_information", "takeaway")

    def create(self, validated_data):
        products = validated_data.pop("products")
        order = Order.objects.create(**validated_data, user=self.context["request"].user)
        order.products.set(products)
        order.save()
        return order


class OrderListRetrieveSerializer(serializers.ModelSerializer):
    products = ProductForOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ("products", "additional_information", "takeaway", "time")
