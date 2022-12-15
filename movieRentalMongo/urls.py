from rest_framework import routers
from .api import DriversLicenseViewSet, MemberViewSet, MovieRentalViewSet, MovieViewSet, RentalViewSet

router = routers.DefaultRouter()

router.register('api/mongo/drivers-license', DriversLicenseViewSet, 'mongo-drivers-license')
router.register('api/mongo/members', MemberViewSet, 'mongo-members')
router.register('api/mongo/movie-rentals', MovieRentalViewSet, 'mongo-movie-rentals')
router.register('api/mongo/movies', MovieViewSet, 'mongo-movies')
router.register('api/mongo/rentals', RentalViewSet, 'mongo-rentals')

urlpatterns = router.urls