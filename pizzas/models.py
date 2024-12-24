from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)