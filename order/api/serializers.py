from rest_framework import serializers
from ..models import Order, OrderItem, PaymentMethod


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "product", "quantity", "created_date", "updated_date")
        read_only_fields = ("product", "created_date", "updated_date")


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ("id", "method", "created_date", "updated_date")
        read_only_fields = ("created_date", "updated_date")


class OrderSerializer(serializers.ModelSerial):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'order_name',
            'user',
            'order_item',
            'payment_method',
            'sub_total_price',
            'tax_price',
            'shipping_price',
            'total_price',
            'is_paid',
            'paid_at',
            'is_delivered',
            'delivered_at',
            'created_date',
            'updated_date'
        )
        read_only_fields = (
            'is_paid',
            'paid_at',
            'created_date',
            'updated_date'
        )
