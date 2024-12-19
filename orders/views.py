from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pizza, Order, Topping
from .serializers import PizzaSerializer, OrderSerializer, ToppingSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

@api_view(['DELETE'])
def delete_pizza(request, pizza_id):
    try:
        pizza = Pizza.objects.get(id=pizza_id)
        pizza.delete()
        return Response({'message': 'Pizza deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Pizza.DoesNotExist:
        return Response({'error': 'Pizza not found.'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def add_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({'message': 'Order deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
def edit_order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        if 'order_status' in request.data:
            order.order_status = request.data['order_status']
            order.save()
            return Response({'message': f'Order status updated successfully.'}, status=status.HTTP_200_OK)
        return Response({'error': 'Order status not provided.'}, status=status.HTTP_400_BAD_REQUEST)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)