from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from orders.views import PizzaViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
