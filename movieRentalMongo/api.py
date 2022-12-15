from movieRentalSQL.models import MovieRental, Movie, DriversLicense, Member, Rental
from rest_framework import viewsets, permissions
from .serializers import DriverLicenseSerializer, MemberSerializer, MovieRentalSerializer, MovieSerializer, RentalSerializer

class MovieRentalViewSet(viewsets.ModelViewSet):
    queryset = MovieRental.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieRentalSerializer

class DriversLicenseViewSet(viewsets.ModelViewSet):
    queryset = DriversLicense.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DriverLicenseSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RentalSerializer