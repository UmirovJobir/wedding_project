from rest_framework import serializers
from services.models import Banquet, BanquetMenu


class BanquetMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanquetMenu
        fields = ('id', 'image', 'name', 'price')

class BanquetSerializer(serializers.ModelSerializer):
    menu = BanquetMenuSerializer(many=True)
    class Meta:
        model = Banquet
        fields = ('id', 'restaurant', 'city', 'address', 'menu')

    def create(self, validated_data):
        menu_data = validated_data.pop('menu')
        banquet = Banquet.objects.create(**validated_data)
        for menu_1 in menu_data:
            BanquetMenu.objects.create(menu_id=banquet, **menu_1)
        return banquet
    
    def update(self, instance, validated_data):
        menu_data = validated_data.pop('menu')
        menu = instance.menu.all()
        menu = list(menu)
        instance.restaurant = validated_data.get('restaurant', instance.restaurant)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        for menu_d in menu_data:
            men = menu.pop(0)
            men.image = menu_d.get('image', men.image)
            men.name = menu_d.get('name', men.name)
            men.price = menu_d.get('price', men.price)
            men.save()
        return instance