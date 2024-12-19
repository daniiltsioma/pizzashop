from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import PizzaViewSet, OrderViewSet, ToppingViewSet, add_order, delete_order, delete_pizza, edit_order_status

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('orders', OrderViewSet)
router.register('toppings', ToppingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/orders/add/', add_order, name='add_order'),
    path('api/orders/delete/<int:order_id>', delete_order, name='delete_order'),
    path('api/orders/edit-status/<int:order_id>', edit_order_status, name='edit-status'),
    path('api/pizzas/delete/<int:pizza_id>', delete_pizza, name='delete_pizza'),
]
