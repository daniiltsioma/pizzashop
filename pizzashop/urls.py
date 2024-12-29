from django.urls import path, include
from rest_framework import routers

from pizzas.views import PizzaViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
