from rest_framework import routers
from . import api
from .api import ReservationViewSet, UserViewSet, PlaceViewSet


router = routers.DefaultRouter()
router.register('api/reservations', api.ReservationViewSet)
router.register('api/users', api.UserViewSet)
router.register('api/places', api.PlaceViewSet)

urlpatterns = router.urls