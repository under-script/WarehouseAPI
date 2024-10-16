from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from api.models import Warehouse


# Serializers define the API representation.
class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        # fields = ['url', 'username', 'email', 'is_staff']
        fields = '__all__'


# Serializers define the API representation.
class PurchaseSerializer(serializers.Serializer):
    product_code = serializers.CharField()
    quantity = serializers.IntegerField()


# Serializers define the API representation.
class CalculateSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_qty = serializers.IntegerField()

class ResultSerializer(serializers.Serializer):
    result = PurchaseSerializer()