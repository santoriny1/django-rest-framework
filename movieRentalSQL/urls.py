from rest_framework import routers
from .api import DriversLicenseViewSet, MemberViewSet, MovieRentalViewSet, MovieViewSet, RentalViewSet

router = routers.DefaultRouter()

router.register('api/sql/drivers-license', DriversLicenseViewSet, 'sql-drivers-license')
router.register('api/sql/members', MemberViewSet, 'sql-members')
router.register('api/sql/movie-rentals', MovieRentalViewSet, 'sql-movie-rentals')
router.register('api/sql/movies', MovieViewSet, 'sql-movies')
router.register('api/sql/rentals', RentalViewSet, 'sql-rentals')

urlpatterns = router.urls