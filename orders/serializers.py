from rest_framework import serializers
from .models import Pizza, Order, OrderItem, PizzaTopping, Topping

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'

class PizzaToppingSerializer(serializers.ModelSerializer):
    topping = ToppingSerializer(read_only=True)
    topping_id = serializers.PrimaryKeyRelatedField(
        queryset=Topping.objects.all(), source='topping', write_only=True
    )

    class Meta:
        model = Topping
        fields = ('topping', 'topping_id')

class PizzaSerializer(serializers.ModelSerializer):
    toppings = PizzaToppingSerializer(many=True)

    class Meta:
        model = Pizza
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('toppings')
        pizza = Pizza.objects.create(**validated_data)
        PizzaTopping.objects.bulk_create(
            [PizzaTopping(pizza=pizza, topping=item['topping']) for item in items_data]
        )
        return pizza
    
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
        fields = ('id', 'customer_name', 'customer_email', 'order_date', 'items', 'order_status')
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