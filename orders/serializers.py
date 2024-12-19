from rest_framework import serializers
from .models import Pizza, Order, OrderItem

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
    items = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'customer_email', 'order_date', 'items')
        read_only_fields = ['order_date']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        OrderItem.objects.bulk_create(
            [OrderItem(order=order, pizza=item['pizza'], quantity=item['quantity']) for item in items_data]
        )
        return order
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = OrderItemSerializer(
            instance.items.all(), many=True
        ).data
        return representation