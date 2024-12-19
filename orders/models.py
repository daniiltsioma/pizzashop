from django.utils.translation import gettext_lazy as _
from django.db import models
from store.models import Store


class Topping(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class PizzaTopping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='toppings')
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        RECEIVED = "R", _("Received")
        PREPARING = "P", _("Preparing")
        COMPLETED = "C", _("Completed")

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=1, choices=OrderStatus.choices, default=OrderStatus.RECEIVED)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.pizza.name} in Order {self.order.id}"