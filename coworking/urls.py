from rest_framework import routers
from . import api


router = routers.DefaultRouter()
router.register('api/reservations', api.ReservationViewSet)
router.register('api/users', api.UserViewSet)
router.register('api/places', api.PlaceViewSet)
router.register('api/bookedTime', api.BookedTimeViewSet)

urlpatterns = router.urls