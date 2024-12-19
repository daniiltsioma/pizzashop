from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Store

from .serializers import EmployeeSerializer, StoreSerializer
from orders.serializers import OrderSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreOrdersListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        store_id = self.kwargs['store_id']
        try:
            store = Store.objects.get(id=store_id)
        except Store.DoesNotExist:
            return Response({'error': 'Store not found.'}, status=status.HTTP_404_NOT_FOUND)
        return store.orders.all()