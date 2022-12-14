from rest_framework import routers
from .api import DriversLicenseViewSet, MemberViewSet, MovieRentalViewSet, MovieViewSet, RentalViewSet

router = routers.DefaultRouter()

router.register('api/drivers-license', DriversLicenseViewSet, 'drivers-license')
router.register('api/members', MemberViewSet, 'members')
router.register('api/movie-rentals', MovieRentalViewSet, 'movie-rentals')
router.register('api/movies', MovieViewSet, 'movies')
router.register('api/rentals', RentalViewSet, 'rentals')

urlpatterns = router.urls