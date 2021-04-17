from .models import Reservation, Place, BookedTime
from rest_framework import viewsets, permissions
from .serializers import ReservationSerializer, UserSerializer, PlaceSerializer, BookedTimeSerializer
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

