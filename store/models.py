from django.utils.translation import gettext_lazy as _
from django.db import models

class Employee(models.Model):
    class EmployeeRole(models.TextChoices):
        EMPLOYEE = "L1", _("Store Employee")
        STORE_MANAGER = "L2", _("Store Manager")
    
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    role = models.CharField(max_length=2, choices=EmployeeRole.choices, default=EmployeeRole.EMPLOYEE)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True) 
    store = models.ForeignKey('Store', on_delete=models.CASCADE, null=True)


class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    manager = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="managed_store", null=True)
