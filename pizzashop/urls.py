from django.urls import path, include
from rest_framework import routers

from pizzas.views import PizzaViewSet

router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
