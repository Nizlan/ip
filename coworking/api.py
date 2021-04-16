from .models import Reservation, Place
from rest_framework import viewsets, permissions
from .serializers import ReservationSerializer, UserSerializer, PlaceSerializer
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

