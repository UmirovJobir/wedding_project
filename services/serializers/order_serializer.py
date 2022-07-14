
from rest_framework import serializers
from services.models import Order


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'restoran', 'menu', 'service', 'gests_amount', 'menu_price', 'service_price', 'total_price', 'status')

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', "user", 'day', 'restoran', 'menu', 'service', 'gests_amount', 'menu_price', 'gests_price_all', 'service_price', 'total_price', 'status')
