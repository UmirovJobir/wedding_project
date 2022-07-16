
from rest_framework import serializers
from services.models.restoran import  RestoranModel, BookedDate, EvantModel, TableModel


class BookedDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedDate
        fields = ('date',)

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = ('id', 'type', 'price', 'restoran_id',)

class RestoranSerializer(serializers.ModelSerializer):
    tables = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    booked_dates = BookedDateSerializer(many=True)

    class Meta:
        model = RestoranModel
        fields = ('id', 'event_id', 'restoran', 'city', 'address', 'booked_dates', 'tables')


class EvantSerializer(serializers.ModelSerializer):
    # restoran_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = EvantModel
        fields = ('id', 'image', 'name', 'active')
