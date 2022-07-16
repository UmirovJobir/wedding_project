
from rest_framework import serializers
from services.models import Order


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'restoran', 'menu', 'table', 'service', 'total_price', 'status')

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', "user_id", 'day', 'restoran', 'table', 'menu', 'service', 'total_price', 'status')
