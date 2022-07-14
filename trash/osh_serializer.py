from dataclasses import field
from re import T
from rest_framework import serializers
from services.models import Osh, OshMenu

class OshMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OshMenu
        fields = ('image', 'name')

class OshSerializer(serializers.ModelSerializer):
    menu = OshMenuSerializer(many=True)

    class Meta:
        model = Osh
        fields = ('id', 'restaurant', 'city', 'address', 'price', 'menu', 'image', 'file')

    def create(self, validated_data):
        menu_data = validated_data.pop('menu')
        osh = Osh.objects.create(**validated_data)
        for menu_1 in menu_data:
            OshMenu.objects.create(menu_id=osh, **menu_1)
        return osh

       