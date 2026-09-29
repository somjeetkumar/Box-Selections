from rest_framework import serializers
from .models import Box, Order, Product, OrderItem


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BoxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]

    def validate_quantity(self, value):

        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "created_at", "items"]

    def validate_items(self, value):

        if not value:
            raise serializers.ValidationError("Order must contain at least one product")
        return value

    def create(self, validated_data):

        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item in items_data:
            OrderItem.objects.create(order=order,**item)

        return order