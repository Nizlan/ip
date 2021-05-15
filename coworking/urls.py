from rest_framework import routers
from . import api


router = routers.DefaultRouter()
router.register('api/reservations', api.ReservationViewSet)
router.register('api/users', api.UserViewSet)
router.register('api/places', api.PlaceViewSet)
router.register('api/bookedTime', api.BookedTimeViewSet)
router.register('api/categories', api.CategoriesViewSet)
router.register('api/availableTime', api.AvailableTimeViewSet)
router.register('api/equipment', api.EquipmentViewSet)
router.register('api/uniqueQualities', api.UniqueQualitiesViewSet)
router.register('api/freeServices', api.FreeServicesViewSet)

urlpatterns = router.urls
