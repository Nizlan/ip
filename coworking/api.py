from services.models import Equipment, UniqueQualities, FreeServices
from .models import Reservation, Place, BookedTime, Categories, AvailableTime
from rest_framework import viewsets, permissions
from .serializers import ReservationSerializer, UserSerializer, PlaceSerializer, BookedTimeSerializer, \
    CategoriesSerializer, AvailableTimeSerializer, EquipmentSerializer, UniqueQualitiesSerializer, \
    FreeServicesSerializer
from django.contrib.auth.models import User


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReservationSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaceSerializer


class BookedTimeViewSet(viewsets.ModelViewSet):
    queryset = BookedTime.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookedTimeSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer


class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AvailableTimeSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer


class UniqueQualitiesViewSet(viewsets.ModelViewSet):
    queryset = UniqueQualities.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UniqueQualitiesSerializer


class FreeServicesViewSet(viewsets.ModelViewSet):
    queryset = FreeServices.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FreeServicesSerializer
