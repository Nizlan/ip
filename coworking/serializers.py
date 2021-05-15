from rest_framework import serializers

from services.models import Equipment, UniqueQualities, FreeServices
from .models import Reservation, Place, BookedTime, Categories, AvailableTime
from django.contrib.auth.models import User


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        depth = 1


class BookedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedTime
        fields = '__all__'
        # depth = 1


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class UniqueQualitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueQualities
        fields = '__all__'


class FreeServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeServices
        fields = '__all__'
