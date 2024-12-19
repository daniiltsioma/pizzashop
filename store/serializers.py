from rest_framework import serializers
from .models import Employee, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'address')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = '__all__'