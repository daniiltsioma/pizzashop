from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import PizzaViewSet, OrderViewSet, ToppingViewSet, add_order, delete_order, delete_pizza, edit_order_status
from store.views import EmployeeViewSet, StoreOrdersListView, StoreViewSet

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('orders', OrderViewSet)
router.register('toppings', ToppingViewSet)
router.register('employees', EmployeeViewSet)
router.register('stores', StoreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/orders/add/', add_order, name='add_order'),
    path('api/orders/delete/<int:order_id>', delete_order, name='delete_order'),
    path('api/orders/edit-status/<int:order_id>', edit_order_status, name='edit-status'),
    path('api/pizzas/delete/<int:pizza_id>', delete_pizza, name='delete_pizza'),
    path('api/stores/<int:store_id>/orders', StoreOrdersListView.as_view(), name='store-orders')
]
