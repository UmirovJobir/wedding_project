
from rest_framework import serializers
from services.models.restoran import MenuItemModel, MenuModel, RestoranModel, BookedDate, EvantModel


class BookedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedDate
        fields = ('date',)

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemModel
        fields = ('id', 'itam_name', 'image', 'menu_id')

class MenuSerializer(serializers.ModelSerializer):
    menuitems = MenuItemSerializer(many=True)
    # menuitems = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = MenuModel
        fields = ('id', 'type', 'price', 'menuitems')

    def create(self, validated_data):
        menuitems_data = validated_data.pop('menuitems')
        menu = MenuModel.objects.create(**validated_data)
        for menuitem_data in menuitems_data:
            MenuItemModel.objects.create(menu_id=menu, **menuitem_data)
        return menu

class RestoranSerializer(serializers.ModelSerializer):
    # menus = MenuSerializer(many=True)
    menus = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    booked_dates = BookedDateSerializer(many=True)

    class Meta:
        model = RestoranModel
        fields = ('id', 'restoran', 'city', 'address', 'booked_dates', 'menus')

    def create(self, validated_data):
        menus_data = validated_data.pop('menus')
        wedding_hall = RestoranModel.objects.create(**validated_data)
        for menu_data in menus_data:
            menuitems_data = menu_data.pop('menuitems')
            menu = MenuModel.objects.create(wedding_hall_id=wedding_hall, **menu_data)
            for menuitem_data in menuitems_data:
                MenuItemModel.objects.create(menu_id=menu, **menuitem_data)
        return wedding_hall

    # def update(self, instance, validated_data):
    #     menus_data = validated_data.pop('menus')
    #     # menus = instance.menus.all()
    #     # menus = list(menus)
    #     instance.wedding_hall = validated_data.get('wedding_hall', instance.wedding_hall)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.save()

    #     for menu_data in menus_data:
    #         menuitems_data = menu_data.pop('menuitems')
    #         items = instance.menus.get().menuitems.all()
    #         items = list(items)
    #         for menuitem_data in menuitems_data:
    #             # item = items.pop(0)
    #             item = MenuItemModel.objects.get(pk=menuitem_data['id'])
    #             item.itam_name = menuitem_data.get('itam_name', item.itam_name)
    #             item.image = menuitem_data.get('image', item.image)
    #             item.save()
    #         # menu = menus.pop(0)
    #         menu = MenuModel.objects.get(pk=menu_data['id'])
    #         menu.type = menu_data.get('type', menu.type)
    #         menu.price = menu_data.get('price', menu.price)
    #         menu.save()
    #     return instance

class EvantSerializer(serializers.ModelSerializer):
    # restorans = RestoranSerializer(many=True)
    restorans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    
    class Meta:
        model = EvantModel
        fields = ('id', 'image', 'name', 'active', 'restorans')
