from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, Pizza
from .serializers import OrderSerializer, PizzaSerializer
from django.utils import timezone

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=["PATCH"])
    def complete_order(self, request, pk=None):
        order = self.get_object()
        order.completed_at = timezone.now()
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)