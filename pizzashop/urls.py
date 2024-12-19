from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import PizzaViewSet, OrderViewSet, add_order, delete_order

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/orders/add/', add_order, name='add_order'),
    path('api/orders/delete/<int:order_id>', delete_order, name='delete_order')
]
