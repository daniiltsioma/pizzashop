from rest_framework import serializers
from .models import Pizza, Order, OrderItem
from django.utils import timezone

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True)
    pizza_id = serializers.PrimaryKeyRelatedField(
        queryset=Pizza.objects.all(), source='pizza', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ('pizza', 'pizza_id', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    items_data = serializers.ListField(
        child=serializers.DictField(),
        write_only=True
    )

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_email', 'items', 'items_data', 'created_at', 'completed_at')

    def create(self, validated_data):
        items_data = validated_data.pop('items_data')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            pizza_id = item_data.get('pizza_id')
            quantity = item_data.get('quantity')
            pizza = Pizza.objects.get(id=pizza_id)

            OrderItem.objects.create(order=order, pizza=pizza, quantity=quantity)
        return order
