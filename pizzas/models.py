from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()

class Order(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
